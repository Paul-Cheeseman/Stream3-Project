# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from products.models import Product
from accounts.models import User
from orders.models import Order, OrderItem
from cart.models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect

#
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

	#variable to determine is restriction is needed to put on HTML input (on product detail page)
	#Done this way as deemed clear for customer to get msg and then have restriction applied
	#than to just limit the form input to stock level max with no indication as to what limit
	#is being applied (although it maybe apparent to some)
	stock_control_max_limit = 0


	#Only process if add URL requested from products page (which will pass these vars)
	if 'product' in request.POST and 'amount' in request.POST:

		product_id = int(request.POST['product'])
		amount_req = request.POST['amount']

		product = get_object_or_404(Product, id=product_id)

		#cater for null/blank value
		if isNotNum(amount_req):
			amount_req = 0




		if 'cart' not in request.session:
			cart = Cart()
			cart.create_cart(request.session)

			#check, if amount is 0, don't add to cart
			if int(amount_req) == 0:
				messages.info(request, "No changes to cart made")          
			else:

				#if product is in stock, set variable to enable add button
				#if the product is product deficite, set variable with amount of stock level to 
				#max level can be put in, update with msg saying contact compnay if need more ASAP
				#go back to product detail page (for that product), need to call it correctly!
				#if Product.in_stock(product_id)
				product = get_object_or_404(Product, id=product_id)
				stock_control_max_limit = product.stock_level_deficite(amount_req)
				if stock_control_max_limit:
					messages.error(request, "Only {0} {1} left in stock, contact support".format(stock_control_max_limit, product.name))
					return render(request, "products/detail.html", {"product": product, "in_stock": product.in_stock(), "stock_control_max_limit": stock_control_max_limit})


				messages.success(request, "Item added to cart")            
				cart.add_to_cart(product_id, amount_req)



		else:

			if 'cart' not in request.session:
				cart = Cart()
				cart.create_cart(request.session)

			else:
				cart = Cart.get_cart(request.session['cart'])

			print(cart.item_in_cart(product_id))

			if int(amount_req) == 0 & (cart.item_in_cart(product_id) !=None):
				cart.remove_from_cart(product_id)
				messages.success(request, "Item removed from cart")          

			elif int(amount_req) == 0:
				messages.info(request, "No changes to cart made")          


			else:

				#if product is in stock, set variable to enable add button
					#if the product is product deficite, set variable with amount of stock level to 
					#max level can be put in, update with msg saying contact compnay if need more ASAP
					#go back to product detail page (for that product), need to call it correctly!
				#if Product.in_stock(product_id)
				product = get_object_or_404(Product, id=product_id)
				stock_control_max_limit = product.stock_level_deficite(amount_req)
				if stock_control_max_limit:
					messages.error(request, "Only {0} {1} left in stock, contact support".format(stock_control_max_limit, product.name))
					return render(request, "products/detail.html", {"product": product, "in_stock": product.in_stock(), "stock_control_max_limit": stock_control_max_limit})


				#Check to see if product already in cart, if so update value
				if cart.item_in_cart(product_id):
					cart.update_cart(product_id, amount_req)
					messages.success(request, "Item quantity in cart updated")            
				else:
					cart.add_to_cart(product_id, amount_req)
					messages.success(request, "Item added to cart")            


	products = Product.objects.all()


	#Get data for dynamically populated drop downs
	#-----------------------------------------------
	category_ddl = Product.objects.values('category').distinct()
	colour_ddl = Product.objects.values('colour').distinct().order_by('colour')
	sizes_ddl = Product.objects.values('size').distinct()
	#Hardcode price ranges
	price_range_ddl = {"Below 2": "Below 2", "Between 2-4": "Between 2-4", "Above 4": "Above 4"}

	

	#Paginating output (if required)
	page = request.GET.get('page', 1)

	#Paginate the products to 2 per page
	paginator = Paginator(products, 3)

	try:
		products_paginated = paginator.page(page)
	except PageNotAnInteger:
		products_paginated = paginator.page(1)
	except EmptyPage:
		products_paginated = paginator.page(paginator.num_pages)


	return render(request, "products/list.html", {"products_paginated": products_paginated, "category_ddl": category_ddl, "price_range_ddl": price_range_ddl, "colour_ddl": colour_ddl, "sizes_ddl": sizes_ddl, "stock_control_max_limit": stock_control_max_limit})


def cart_list(request):

	#variable to determine is restriction is needed to put on HTML input
	#Done this way as deemed clear for customer to get msg and then have restriction applied
	#than to just limit the form input to stock level max with no indication as to what limit
	#is being applied (although it maybe apparent to some)
	stock_control_max_limit = 0

	if 'cart' in request.session:
		print("Cart detected")
		cart = Cart.get_cart(request.session['cart'])

		#default setting to show cart delete button on form when have a cart
		delete_button_show = True

		if 'delete' in request.POST:
			#remove items from CartItem table

			cart.del_cart(request)
			#prevent the HTML for the delete button being generated
			delete_button_show = False
			messages.error(request, "Cart deleted")

		#Determine is the page is initially loading or user is submitting form
		if 'product' in request.POST and 'amount' in request.POST:
			product_id = int(request.POST['product'])
			amount_req = request.POST['amount']
			cart.update_cart(product_id, amount_req)


			#if product is in stock, set variable to enable add button
				#if the product is product deficite, set variable with amount of stock level to 
					#max level can be put in, update with msg saying contact compnay if need more ASAP
					#go back to product detail page (for that product), need to call it correctly!
				#if Product.in_stock(product_id)
			product = get_object_or_404(Product, id=product_id)
			stock_level_warning = product.stock_level_deficite(amount_req)
			if stock_level_warning:
				messages.error(request, "Only {0} {1} left in stock, contact support".format(stock_level_warning, product.name))
				stock_control_max_limit = stock_level_warning


			if not cart.items_in_cart():
				messages.info(request, "No items in cart")
				cart.del_cart(request)
				delete_button_show = False

		products = cart.add_quantity()

	else:

		products = {}
		messages.info(request, "No items in cart")
		#prevent the HTML for the delete button being generated	
		delete_button_show = False

	return render(request, "cart/cart.html", {"products": products, "delete_button_show": delete_button_show, "stock_control_max_limit": stock_control_max_limit})

