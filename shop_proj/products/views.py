# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product



#Change to list all 
def products(request):

	#Get all Products from DB for display
	products = Product.objects.all()


	if request.GET.get('name') == "reverse":
		products = Product.objects.order_by('-name')
		name = ""
	else:
		products = Product.objects.order_by('name')
		name = "reverse"
		#print("name")
		#print(name)



	if request.GET.get('category'):
		print("category")
		print(request.GET.get('category'))



#	elif request.GET.get('price'):
#		print("price")


#	elif request.GET.get('reset'):
#		print("reset")
	

	#list of categories for drop down search
	category_ddl = Product.objects.values('category').distinct()

	#list of price ranges
	price_range_ddl = {"Below £15": "Below £15", "Between £15-40": "Between £15-40", "Above £40": "Above £40"}

	return render(request, "products/products.html", {"products": products, "category_ddl": category_ddl, "price_range_ddl": price_range_ddl, "name": name})



def sort_prod_alpha(request):
	#first 'get' is blank so sorted decendingly first
	if request.GET.get('reverse') == "true":
		reverse = "false"
		sorted_products = Product.objects.order_by('-name')		
	else:
		reverse = "true"
		sorted_products = Product.objects.order_by('name')

	return render(request, "products/products.html",  {"products": sorted_products, "reverse": reverse})


def sort_prod_price(request):
	sorted_products = Product.objects.order_by('price')		
	return render(request, "products/products.html",  {"products": sorted_products})


def filtered_cat(request):
	cat_filter = request.GET.get('pd')
	filtered_category = Product.objects.filter(category=cat_filter)		
	return render(request, "products/products.html",  {"products": filtered_category})


