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

#just some rubbish to get site running to test something before tidying up
def get_index(request):
	#just some rubbish to get site running to test something before tidying up
	return render(request, "index.html")

#just some rubbish to get site running to test something before tidying up
def get_new_index(request):
	#just some rubbish to get site running to test something before tidying up
	return render(request, "index-new.html")


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


	return render(request, "products/products.html", {"products_paginated": products_paginated, "category_ddl": category_ddl, "price_range_ddl": price_range_ddl, "colour_ddl": colour_ddl, "sizes_ddl": sizes_ddl})


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

