# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product



#Change to list all 
def all_products(request):
	products = Product.objects.all()
	return render(request, "products/products.html", {"products": products})





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


