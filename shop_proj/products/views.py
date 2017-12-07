# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Product



#Change to list all 
def products(request):

	print("get")
	print(request.GET.get)

	if request.GET.get('name') == "reverse":
		products = Product.objects.order_by('-name')
		name = ""
	else:
		products = Product.objects.order_by('name')
		name = "reverse"


	if request.GET.get('category'):
		if request.GET.get('category') == "all":
			products = Product.objects.all()
		else:
			cat_filter = request.GET.get('category')
			products = Product.objects.filter(category=cat_filter)


	if request.GET.get('price'):
		price2 = request.GET.get('price')
		if price2 == "all":
			products = Product.objects.all()
		else:
			if price2 == "Below 2":
				products = Product.objects.filter(price__lt = 2.00)
			elif price2 == "Between 2-4":
				products = Product.objects.filter(price__lte = 4.00).filter(price__gte = 2.00)
			elif price2 == "Above 4":
				products = Product.objects.filter(price__gt = 4)				

	category_ddl = Product.objects.values('category').distinct()
	#list of price ranges
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


	return render(request, "products/products.html", {"products_paginated": products_paginated, "category_ddl": category_ddl, "price_range_ddl": price_range_ddl, "name": name})








def product_detail(request):
		if request.GET.get('product_name'):
			print("Product Name:")
			print(request.GET.get('product_name'))
			product_name = request.GET.get('product_name')

			#product_details = get_object_or_404(Product, name=product_name)
			product = get_object_or_404(Product, name="Product 1")



		return render(request, "products/product_detail.html", {"product": product})
