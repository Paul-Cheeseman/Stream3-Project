# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages


import stripe

	#just some rubbish to get site running to test something before tidying up
	#just some rubbish to get site running to test something before tidying up
	#just some rubbish to get site running to test something before tidying up
	#just some rubbish to get site running to test something before tidying up
	#just some rubbish to get site running to test something before tidying up
	#just some rubbish to get site running to test something before tidying up
def get_index(request):
	#just some rubbish to get site running to test something before tidying up
	return render(request, "index.html")




def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False




#Change to list all 
def cart_add(request):

	#Only process if add URL requested from products page (which will pass these vars)
	if 'product' in request.POST and 'amount' in request.POST:

		product_id = request.POST['product']
		amount_req = request.POST['amount']

		#cater for null value
		if isNum(amount_req):
			print("numeric")
		else:
			amount_req = 0
			print("null to 0")


		if 'cart' not in request.session:
			print("Cart created")
			cart = Cart()
			#create cart in db
			cart.save()
			request.session['cart'] = cart.id

			#check, if amount is 0, don't add to cart
			if amount_req != 0:
				product_to_add = Product.objects.get(id=product_id)
				cartItem = CartItem(cart=cart, product=product_to_add, amount=amount_req)
				cartItem.save()

		else:

			if int(amount_req) == 0:
				#Check to see if product already in cart, if so set value to 0
				checking_queryset = CartItem.objects.filter(cart_id=request.session['cart'])
				for item in checking_queryset:

					if item.product_id == int(product_id):
						CartItem.objects.filter(id=item.id).delete()

			else:

				#Check to see if product already in cart, if so update value
				checking_queryset = CartItem.objects.filter(cart_id=request.session['cart'], product_id=product_id)
				if checking_queryset.exists():
					print("item already in cart")
					for item in checking_queryset:
						if item.product_id == int(product_id):
							item.amount = amount_req
							item.save()

				else:
					print("new item for cart")
					product_to_add = Product.objects.get(id=product_id)

					cart = Cart.objects.get(id=request.session['cart'])
					
					cartItem = CartItem(cart=cart, product=product_to_add, amount=amount_req)
					cartItem.save()

				#This is testing, put this at checkout and logout
				#del request.session['cart']

	products = Product.objects.all()

	return render(request, "products/products.html", {"products": products})



def cart_update(request):

	#Only process if add URL requested from products page (which will pass these vars)
	if 'product' in request.POST and 'amount' in request.POST:

		product_id = request.POST['product']
		amount_req = request.POST['amount']

		#cater for null value
		if isNum(amount_req):
			print("numeric")
		else:
			amount_req = 0
			print("null to 0")


		if int(amount_req) == 0:
			#Check to see if product already in cart, if so set value to 0
			checking_queryset = CartItem.objects.filter(cart_id=request.session['cart'], product_id=product_id)
			if checking_queryset.exists():
				CartItem.objects.filter(cart_id=request.session['cart'], product_id=product_id).delete()

		else:

			#Check to see if product already in cart, if so update value
			checking_queryset = CartItem.objects.filter(cart_id=request.session['cart'], product_id=product_id)
			if checking_queryset.exists():
				print("item already in cart")
				for item in checking_queryset:
					if item.product_id == int(product_id):
						item.amount = amount_req
						item.save()


			#This is testing, put this at checkout and logout
			#del request.session['cart']

	#Select all records from Cart_Item for current id
	items_in_cart = CartItem.objects.filter(cart_id=request.session['cart'])		

	#for each cart item, use the stored product_id to retrive product details from product table
	products = Product.objects.filter(id__in=[item.product_id for item in items_in_cart])

	#getting amount ordered of each product so can auto-fill cart list
	for item in products:
		cartItem_amount = CartItem.objects.get(product_id=item.id)
		item.amount = cartItem_amount.amount

	return render(request, "cart/cart.html", {"products": products})




#Change to list all 
def cart_list(request):

	if 'cart' in request.session:
		
		#Select all records from Cart_Item for current id
		items_in_cart = CartItem.objects.filter(cart_id=request.session['cart'])		

		#for each cart item, use the stored product_id to retrive product details from product table
		products = Product.objects.filter(id__in=[item.product_id for item in items_in_cart])

		#getting amount ordered of each product so can auto-fill cart list
		for item in products:
			cartItem_amount = CartItem.objects.get(product_id=item.id)
			item.amount = cartItem_amount.amount

		return render(request, "cart/cart.html", {"products": products})

	return render(request, "cart/cart.html")




#remove from cart
def cart_del(request):

	if 'cart' in request.session:

		#remove items from CartItem table
		items_in_cart = CartItem.objects.filter(cart_id=request.session['cart'])
		for item in items_in_cart:
				CartItem.objects.filter(id=item.id).delete()

		#remove from Cart table
		Cart.objects.filter(id=request.session['cart']).delete()		

		#delete session key
		del request.session['cart']


	#send customers to products page (with all products) after cart deletion
	products = Product.objects.all()
	return render(request, "products/products.html", {"products": products})





#User has to be logged in to checkout
@login_required(login_url='/login/') 
def checkout(request):

	messages.error(request, "Msgs on")
	#assume credit card not record until proven otherwise
	cc_reg = "btn btn-sm btn-success disabled"

	user = User.objects.get(username=request.user)

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
			cartItem_amount = CartItem.objects.get(product_id=item.id)
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
				messages.error(request, "Please register an address")

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
					#disable button
					#msg to say payment submitted
					#on successful payment, go to another screen
					new_order = Order()
					new_order.save()

					customer = User.objects.get(username=request.user)
					
					for item in products:
						print("item cost post order!")
						print(item.cost)
						new_orderItem = OrderItem(order_id=new_order, product=item, quantity=item.amount, price=item.price, customer=user, address_line1=user.address_line1, address_line2=user.address_line2, county=user.county, postcode=user.postcode)
						new_orderItem.save()






					#### Put in order
					### Then orders page for customer
					### Then done!!!












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

