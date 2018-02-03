# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import stripe

from accounts.models import User
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem
from products.models import Product


#User has to be logged in to checkout
@login_required() 
def checkout(request):

	#assume credit card not recorded for customer until proven otherwise
	cc_reg = "btn btn-sm btn-success disabled"
	#get user object
	user = get_object_or_404(User, username=request.user)

	#set cost and amount variables
	global total_cost
	total_cost = 0
	total_amount = 0	
	delivery_cost = 0

	#if basket present
	if 'cart' in request.session:

		#Select all records from Cart_Item for current id
		items_in_cart = CartItem.objects.filter(cart_id=request.session['cart'])		

		#for each cart item, use the stored product_id to retrive product details from product table
		products = Product.objects.filter(id__in=[item.product_id for item in items_in_cart])

		#getting amount ordered of each product so can auto-fill checkout list
		for item in products:
			cartItem_amount = get_object_or_404(CartItem, product_id=item.id, cart_id=request.session['cart'])
			item.amount = cartItem_amount.amount
			item.cost = item.amount * item.price
			total_cost = total_cost + item.cost
			total_amount = total_amount + item.amount
			pence_cost = int(total_cost * 100)

		#add £2 deliver charge per item
		delivery_cost = total_amount * 2
		total_cost = total_cost + delivery_cost


		if items_in_cart.exists():

			#Check that credit card and address have been logged before allowing checkout (and enabling purchase button)
			if user.stripe_custID == "None":
				messages.error(request, "Please register a credit card before attempting purchase")

			elif user.address_line1 == "None" or user.address_line2 == "None" or user.county == "None" or user.postcode == "None":
				messages.error(request, "Please register a complete address")

			else:
				#enable purchase button
				cc_reg = "btn btn-sm btn-success"

				#if request method is POST some is trying to buy product
				if 'purchase' in request.POST:
					#set cost and amount variables to check if checkout amounts needs to be refreshed at checkout.
					#
					#On a multi-user system for a company with relatively small stock levels, between the customer
					#putting item(s) in cart and getting to checkout, their is the real risk that another customer purchase 
					#could pull stock levels down to a level where the current customers order can't be met with existing
					#stock. This would then require extra time to restock, so the company would prefer the customer call them
					#so they can speak through the options.
					total_cost_refresh = 0
					total_amount_refresh = 0	
					delivery_cost_refresh = 0

					#Go through and check stock levels are still OK pre purchase
					#i.e has another customer made a purchase and reduced available stock levels below what can be fulfilled?
					refresh_checkout = False

					for item in products:
						#Need to get current stock level
						current_product = get_object_or_404(Product, id=item.id)
						if item.amount > current_product.stock_level:
							refresh_checkout = True
							#Get the object that hold this amount value
							cartItem = get_object_or_404(CartItem, product_id=item.id, cart_id=request.session['cart'])
							#set it to the stock leve value (so that 'refresh_checkout' won't be true 2nd time around)
							cartItem.amount = current_product.stock_level
							#save it to database
							cartItem.save()
							#Also change value of item being iterated over
							item.amount = current_product.stock_level

						item.cost = item.amount * item.price
						total_cost_refresh = total_cost_refresh + (item.amount * item.price)
						total_amount_refresh = total_amount_refresh + item.amount

					#£2 deliver charge per item
					delivery_cost_refresh = total_amount_refresh * 2
					total_cost_refresh = total_cost_refresh + delivery_cost_refresh

		
					if refresh_checkout == True:
						messages.error(request, "Other recent customer purchases mean we can no longer currently meet you order with our existing stock, your order has been updated to reflect current stock levels. Please contact us to discuss acquiring the additional items.")

						#Need to amend cartItem to store new amount value, so that if purchase not made 
						#but cart stored, the item is not deleted (on signing back in) unless 
						#stock levels has actually gone below the amended amount 
						cart_item = get_object_or_404(items_in_cart, product_id=item.id)
						cart_item.amount = current_product.stock_level
						cart_item.save()

						return render(request, "checkout/checkout.html", {"user": user, "products": products, "cc_reg": cc_reg, "total_cost": total_cost_refresh, "total_amount": total_amount_refresh, "delivery_cost": delivery_cost_refresh})


					try:
						#Try to make payment!
						charge = stripe.Charge.create(
  							amount=pence_cost,
  							currency="gbp",
  							customer=user.stripe_custID,
						)
						messages.success(request, "Payment Successful")

						#Create order entries in database
						customer = get_object_or_404(User, username=request.user)
						new_order = Order(address_line1=user.address_line1, address_line2=user.address_line2, county=user.county, postcode=user.postcode, total=(pence_cost/100), customer_id=customer.id)
						new_order.save()
					
						for item in products:
							new_orderItem = OrderItem(order_id=new_order.id, product=item, quantity=item.amount, price=item.price)
							new_orderItem.save()

							#Reduce the stock level
							#The amount won't be bigger than current stock levels due to pre-purchase stock
							#level checks (so no need to check here)
							current_product = get_object_or_404(Product, id=item.id)
							current_product.stock_level = current_product.stock_level - item.amount
							current_product.save()

						#"When Django deletes an object, by default it emulates the behavior of the SQL constraint ON DELETE 
						#CASCADE – in other words, any objects which had foreign keys pointing at the object to be deleted 
						#will be deleted along with it". So this command should remove the cart and associated cart items 
						#from the database.
						Cart.objects.filter(id=request.session['cart']).delete()
						del request.session['cart']

						#If the cart was from a stored version, remove it
						if user.saved_cart_id != 0:
							user.saved_cart_id = 0
							user.save()

						#Send user to orders page after successful purchase
						return redirect("orders")					

					#Gracefully catch error, inform customer of issue
					except stripe.error.CardError as e:
						body = e.json_body
						err  = body.get('error', {})
						messages.error(request, err.get('message'))
				else:
					#this is enabling purchase button on initial page load (rather than when purchase has been pressed)
					#when credit card and address have been stored in database.
					cc_reg = "btn btn-sm btn-success"

			return render(request, "checkout/checkout.html", {"user": user, "products": products, "cc_reg": cc_reg, "total_cost": total_cost, "total_amount": total_amount, "delivery_cost": delivery_cost})

		#empty cart, let use rknow
		else:
			messages.error(request, "Nothing in your cart, please add an item before attempting purchase")
			return render(request, "checkout/checkout.html", {"cc_reg": cc_reg,  "total_cost": total_cost, "total_amount": total_amount, "delivery_cost": delivery_cost})

	else:
		messages.error(request, "You don't have a cart yet, please create one by adding an item before attempting purchase")
		return render(request, "checkout/checkout.html", {"cc_reg": cc_reg,  "total_cost": total_cost, "total_amount": total_amount, "delivery_cost": delivery_cost})
