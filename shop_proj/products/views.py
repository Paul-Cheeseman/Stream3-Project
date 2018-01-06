# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Product



#Change to list all 
def products(request):

	if request.GET.get('resetall') == "y":

		#Determines descending/ascending order of products by name
		order = ""

		product_filter = Product.objects.all()


	else:

		product_filter = Product.objects.all()


		if request.GET.get('category'):
			cat_filter = request.GET.get('category')
			product_filter = Product.objects.filter(category=cat_filter)


		if request.GET.get('price'):
			price = request.GET.get('price')
			if not product_filter.exists():
				product_filter = Product.objects
			if price == "Below 2":
				product_filter = product_filter.filter(price__lt = 2.00)
			elif price == "Between 2-4":
				product_filter = product_filter.filter(price__lte = 4.00).filter(price__gte = 2.00)
			elif price == "Above 4":
				product_filter = product_filter.filter(price__gt = 4)				

		if request.GET.get('name') == "reverse":
			product_filter = product_filter.order_by('-name')
			order = ""
		else:
			product_filter = product_filter.order_by('name')
			order = "reverse"

		if request.GET.get('gender'):
			get_gender = request.GET.get('gender')
			product_filter = product_filter.filter(gender=get_gender)


		if request.GET.get('colour'):
			get_colour = request.GET.get('colour')
			product_filter = product_filter.filter(colour=get_colour)


		if request.GET.get('size'):
			get_size = request.GET.get('size')
			product_filter = product_filter.filter(size=get_size)


		if request.GET.get('age'):
			get_age = request.GET.get('age')
			product_filter = product_filter.filter(age=get_age)



		if not product_filter.exists():
			messages.info(request, "No products to display - you've filtered them all out!")

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
	paginator = Paginator(product_filter, 3)

	try:
		products_paginated = paginator.page(page)
	except PageNotAnInteger:
		products_paginated = paginator.page(1)
	except EmptyPage:
		products_paginated = paginator.page(paginator.num_pages)


	return render(request, "products/list.html", {"products_paginated": products_paginated, "category_ddl": category_ddl, "price_range_ddl": price_range_ddl, "colour_ddl": colour_ddl, "sizes_ddl": sizes_ddl, "order": order,})





def product_detail(request):
	if request.GET.get('product_name'):
		product_name = request.GET.get('product_name')

		#product_details = get_object_or_404(Product, name=product_name)
		product = get_object_or_404(Product, name=product_name)

		return render(request, "products/detail.html", {"product": product, "in_stock": product.in_stock()})
