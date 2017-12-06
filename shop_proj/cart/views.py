# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import stripe


#just some rubbish to get site running to test something before tidying up
def get_index(request):
	#just some rubbish to get site running to test something before tidying up
	return render(request, "index.html")



def isNotNum(data):
    try:
        int(data)
        return False
    except ValueError:
        return True



#Change to list all 
def cart_add(request):

	#Only process if add URL requested from products page (which will pass these vars)
	if 'product' in request.POST and 'amount' in request.POST:

		product_id = int(request.POST['product'])
		amount_req = request.POST['amount']

		#cater for null/blank value
		if isNotNum(amount_req):
			amount_req = 0

		if 'cart' not in request.session:
			cart = Cart()
			cart.create_cart(request.session)

			#check, if amount is 0, don't add to cart
			if amount_req != 0:
				cart.add_to_cart(product_id, amount_req)

		else:
			#put this here to reduce repeating code
			cart = Cart.get_cart(request.session['cart'])

			if int(amount_req) == 0:
				cart.remove_from_cart(product_id)

			else:
				#Check to see if product already in cart, if so update value
				if cart.item_in_cart(product_id):
					cart.update_cart(product_id, amount_req)
				else:
					cart.add_to_cart(product_id, amount_req)

	products = Product.objects.all()

	return render(request, "products/products.html", {"products": products})



def cart_list(request):
	if 'cart' in request.session:
		print("Cart detected")
		cart = Cart.get_cart(request.session['cart'])

		#default setting to show cart delete button on form when have a cart
		delete_button_show = True

		if 'delete' in request.POST:
			print("Delete activated!")
			#remove items from CartItem table

			cart.del_cart(request)
			messages.error(request, "As requested Cart Deleted!")
			#prevent the HTML for the delete button being generated
			delete_button_show = False


		#Determine is the page is initially loading or user is submitting form
		if 'product' in request.POST and 'amount' in request.POST:
			product_id = int(request.POST['product'])
			amount_req = request.POST['amount']
			cart.update_cart(product_id, amount_req)

			if not cart.items_in_cart():
				cart.del_cart(request)
				messages.error(request, "Cart Removed as no items within it!")
				delete_button_show = False

		products = cart.add_quantity()

	else:
		products = {}
		#prevent the HTML for the delete button being generated	
		delete_button_show = False

	return render(request, "cart/cart.html", {"products": products, "delete_button_show": delete_button_show})





#User has to be logged in to checkout
@login_required(login_url='/login/') 
def checkout(request):

	messages.error(request, "Msgs on")
	#assume credit card not record until proven otherwise
	cc_reg = "btn btn-sm btn-success disabled"

	user = get_object_or_404(User, username=request.user)

	#if basket present
	if 'cart' in request.session:
		messages.error(request, ", got cart")
		#Select all records from Cart_Item for current id
		items_in_cart = CartItem.objects.filter(cart_id=request.session['cart'])		

		#for each cart item, use the stored product_id to retrive product details from product table
		products = Product.objects.filter(id__in=[item.product_id for item in items_in_cart])
		#getting amount ordered of each product so can auto-fill cart list

		#Timmy Help
		global total_cost
		total_cost = 0

		for item in products:
			cartItem_amount = get_object_or_404(CartItem, product_id=item.id, cart_id=request.session['cart'])
			item.amount = cartItem_amount.amount
			item.cost = item.amount * item.price
			total_cost = total_cost + item.cost

			pence_cost = int(total_cost * 100)
		#Don't process is customer has a cart but nothing in it, tell them
		#if anything in basket?
		if items_in_cart.exists():
			messages.error(request, ", items in cart")
			#if credit card stored?
			if user.stripe_custID == "None":
				messages.error(request, "Please register a credit card before attempting purchase")

			elif user.address_line1 == "None" or user.address_line2 == "None" or user.county == "None" or user.postcode == "None":
				messages.error(request, "Please register a complete address")

			else:
				cc_reg = "btn btn-sm btn-success"
				messages.error(request, ", got Credit card")

				#if POST
				if 'purchase' in request.POST:
					
					#make payment
					charge = stripe.Charge.create(
  						amount=pence_cost,
  						currency="gbp",
  						customer=user.stripe_custID,
					)
					messages.error(request, "Payment Made! - Go to orders Page, delete cart etc")


					#Create order entries
					new_order = Order()
					new_order.save()
					customer = get_object_or_404(User, username=request.user)
					

					for item in products:
						print("item cost post order!")
						print(item.cost)
						new_orderItem = OrderItem(order_id=new_order.id, product=item, quantity=item.amount, price=item.price, customer=user, address_line1=user.address_line1, address_line2=user.address_line2, county=user.county, postcode=user.postcode)
						new_orderItem.save()

					#remove cartItems from database and cart from session


					cartItems_to_rem = CartItem.objects.filter(cart_id=request.session['cart'])



					for item in cartItems_to_rem:
						#item_to_go = CartItem.objects.get(cart_id=request.session['cart'])
						#item_to_go.delete()
						item.delete()


					#remove cart from database and session
					print("cart id:")
					print(request.session['cart'])
					get_object_or_404(Cart, id=request.session['cart']).delete()
					del request.session['cart']


					return render(request, "cart/checkout.html")					
	

				else:
					cc_reg = "btn btn-sm btn-success"

			return render(request, "cart/checkout.html", {"user": user, "products": products, "cc_reg": cc_reg, "total_cost": total_cost})


		else:
			messages.error(request, "Nothing in your cart, please add an item before attempting purchase")
			return render(request, "cart/checkout.html", {"cc_reg": cc_reg})

	else:
		messages.error(request, "You don't have a cart yet, please create one by adding an item before attempting purchase")
		return render(request, "cart/checkout.html", {"cc_reg": cc_reg})
	#Need name, address etc for customer, if not redirect to profile page
	#Passing user details across

