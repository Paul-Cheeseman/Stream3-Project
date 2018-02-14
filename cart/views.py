# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404,  redirect

from accounts.models import User
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem
from products.models import Product


#Helper function to detemine if value passed is an Integer
def isNotNum(data):
    try:
        int(data)
        return False
    except ValueError:
        return True



def cart_add(request):
	#Variable to determine is restriction is needed to put on HTML input (on product detail page)
	#Done this way as deemed clearer for customer to get msg and then have restriction applied
	#than to just limit the form input to stock level max with no indication as to why a limit
	#is being applied (although it maybe apparent some customers!)
	stock_control_max_limit = 0

	#Only process if add URL requested from products page (which will pass these vars)
	if 'product' in request.POST and 'amount' in request.POST:

		product_id = int(request.POST['product'])
		amount_req = request.POST['amount']
		product = get_object_or_404(Product, id=product_id)

		#cater for null/blank value being passed
		if isNotNum(amount_req):
			amount_req = 0

		#if cart not in request.session, create a new one
		if 'cart' not in request.session:
			cart = Cart()
			cart.create_cart(request.session)

			#if amount is 0, don't add to cart
			if int(amount_req) == 0:
				messages.info(request, "No changes to cart made")          
			else:
				#if the user request is higher than the amount in stock set 'stock_control_max_limit' variable 
				# to the stock level amount, which wil then be used as a max value for form. In addition produce
				#a msg saying contact company if need to arrange more than are currently in stock
				#reload page before the item(s) is/are added to cart
				product = get_object_or_404(Product, id=product_id)
				stock_control_max_limit = product.stock_level_deficite(amount_req)
				if stock_control_max_limit:
					messages.error(request, "Only {0} {1} left in stock, please contact us if you need more".format(stock_control_max_limit, product.name))
					return render(request, "products/detail.html", {"product": product, "in_stock": product.in_stock(), "stock_control_max_limit": stock_control_max_limit})

				#Only add to cart if customer is ordering an amount at or below current stock levels
				cart.add_to_cart(product_id, amount_req)

				#Ensure the customer knows that additional steps are required if using site when not authenticated
				if not request.user.is_authenticated:
					messages.error(request, "Please be aware you will need to login (or register) to complete your order")					
		else:
			#if cart not in request.session, create a new one
			if 'cart' not in request.session:
				cart = Cart()
				cart.create_cart(request.session)

			else:
				#get cart object which has the cart id stored in the session variable
				cart = Cart.get_cart(request.session['cart'])

			#if the user enters 0 or blank in the value fields, treat as a request to remove that item from the cart
			if int(amount_req) == 0 & (cart.item_in_cart(product_id) !=None):
				cart.remove_from_cart(product_id)

			else:

				#if the user request is higher than the amount in stock set 'stock_control_max_limit' variable 
				# to the stock level amount, which wil then be used as a max value for form. In addition produce
				#a msg saying contact company if need to arrange more than are currently in stock
				#reload page before the item(s) is/are added to cart
				product = get_object_or_404(Product, id=product_id)
				stock_control_max_limit = product.stock_level_deficite(amount_req)
				if stock_control_max_limit:
					messages.error(request, "Only {0} {1} left in stock, please contact us if you need more".format(stock_control_max_limit, product.name))
					return render(request, "products/detail.html", {"product": product, "in_stock": product.in_stock(), "stock_control_max_limit": stock_control_max_limit})

				#Check to see if product already in cart, if so update value
				if cart.item_in_cart(product_id):
					cart.update_cart(product_id, amount_req)
					#messages.success(request, "Item quantity in cart updated")            
				else:
					cart.add_to_cart(product_id, amount_req)
					#messages.success(request, "Item added to cart")            

	#return a full list of products
	products = Product.objects.all()


	#Get data for dynamically populated drop downs
	#category_ddl = Product.objects.values('category').distinct()
	#Catering for Django distinct() not working when being used on SQL (which it is LIVE)
	category_ddl_group = Product.objects.values('category').order_by('category')
	category_ddl = []
	for item in category_ddl_group:
		if not item in category_ddl:
			category_ddl.append(item)
	
	#colour_ddl = Product.objects.values('colour').distinct().order_by('colour')
	#Catering for Django distinct() not working when being used on SQL (which it is LIVE)
	colour_ddl_group = Product.objects.values('colour').order_by('colour')
	colour_ddl = []
	for item in colour_ddl_group:
		if not item in colour_ddl:
			colour_ddl.append(item)


	#sizes_ddl = Product.objects.values('size').distinct()
	#Catering for Django distinct() not working when being used on SQL (which it is LIVE)
	sizes_ddl_group = Product.objects.values('size').order_by('size').reverse()
	sizes_ddl = []
	for item in sizes_ddl_group:
		if not item in sizes_ddl:
			sizes_ddl.append(item)


	price_range_ddl = {"Below 5": "Below 5", "Between 5-20": "Between 5-20", "Above 20": "Above 20"}

	
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
	#Variable to determine is restriction is needed to put on HTML input (on product detail page)
	#Done this way as deemed clearer for customer to get msg and then have restriction applied
	#than to just limit the form input to stock level max with no indication as to why a limit
	#is being applied (although it maybe apparent some customers!)
	stock_control_max_limit = 0
	products = {}

	if 'cart' in request.session:
		cart = Cart.get_cart(request.session['cart'])

		#Inform user if they have an empty cart
		if not cart.items_in_cart():
			messages.info(request, "No items in cart")
			cart.del_cart(request)
			delete_button_show = False

		else: 

			#default setting to show cart delete button on form when have a cart
			delete_button_show = True

			#removing item from cart
			if 'delete' in request.POST:
				#remove items from CartItem table
				cart.del_cart(request)
				#prevent the HTML for the delete button being generated
				delete_button_show = False
				#messages.error(request, "Cart deleted")

			#Determine is the page is initially loading or user is submitting form
			if 'product' in request.POST and 'amount' in request.POST:
				product_id = int(request.POST['product'])
				amount_req = request.POST['amount']

				#if the user request is higher than the amount in stock set 'stock_control_max_limit' variable 
				# to the stock level amount, which wil then be used as a max value for form. In addition produce
				#a msg saying contact company if need to arrange more than are currently in stock
				#reload page before the item(s) is/are added to cart
				product = get_object_or_404(Product, id=product_id)
				product.stock_level_warning = product.stock_level_deficite(amount_req)
				if product.stock_level_warning:
					messages.error(request, "Only {0} {1} left in stock, please contact us if you need more".format(product.stock_level_warning, product.name))
					cart.update_cart(product_id, product.stock_level_warning)

				else:
					cart.update_cart(product_id, amount_req)

		#Adding quantity to any products in cart
		products = cart.add_quantity()


	else:
		#inform customer is they have an empty cart
		messages.info(request, "No items in cart")
		#prevent the HTML for the delete button being generated	
		delete_button_show = False

	return render(request, "cart/cart.html", {"products": products, "delete_button_show": delete_button_show})

