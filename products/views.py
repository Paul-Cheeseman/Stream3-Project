# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Product



#Change to list all 
def products(request):
	if request.GET.get('resetall') == "y":
		#Determines descending/ascending order of products by name
		order = ""

		#produce a queryset will all products in it for reset 
		product_filter = Product.objects.all()

	else:

		#Get full queryset, then apply the filters as per request.get
		#Set up a series of IF's as the filtering needs to be accumulative
		product_filter = Product.objects.all()

		if request.GET.get('category'):
			cat_filter = request.GET.get('category')
			product_filter = Product.objects.filter(category=cat_filter)

		if request.GET.get('price'):
			price = request.GET.get('price')
			if not product_filter.exists():
				product_filter = Product.objects
			if price == "Below 5":
				product_filter = product_filter.filter(price__lt = 5.00)
			elif price == "Between 5-20":
				product_filter = product_filter.filter(price__lte = 20.00).filter(price__gte = 5.00)
			elif price == "Above 20":
				product_filter = product_filter.filter(price__gt = 20)				

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

	#Paginate the products to 5 per page
	paginator = Paginator(product_filter, 5)

	try:
		products_paginated = paginator.page(page)
	except PageNotAnInteger:
		products_paginated = paginator.page(1)
	except EmptyPage:
		products_paginated = paginator.page(paginator.num_pages)


	return render(request, "products/list.html", {"products_paginated": products_paginated, "category_ddl": category_ddl, "price_range_ddl": price_range_ddl, "colour_ddl": colour_ddl, "sizes_ddl": sizes_ddl, "order": order,})





def product_detail(request):
	if request.GET.get('product_name'):
		#get and return the product detail object
		product_name = request.GET.get('product_name')
		product = get_object_or_404(Product, name=product_name)

		return render(request, "products/detail.html", {"product": product, "in_stock": product.in_stock()})
