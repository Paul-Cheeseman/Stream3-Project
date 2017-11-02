# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product

# Create your views here.


#Change to list all 
def all_products(request):
	products = Product.objects.all()
	return render(request, "products/products.html", {"products": products})



def basket_add(request):
	product = request.POST['product']
	amount = request.POST['amount']	

 	cart = request.session.get('cart', {})
 	
 	print amount

 	if int(amount) == 0:
 		print "zero val"
		cart.pop(product)
 	else: 
 		cart[product] = amount
		request.session['cart'] = cart

	print request.session['cart']



	for item in cart:
		print item, cart[item]


	products = Product.objects.all()
	return render(request, "products/products.html", {"products": products})


def basket_list(request):

	products = Product.objects.all()		
	return render(request, "products/products.html",  {"products": products})      





def sort_prod_alpha(request):
	print request.GET.get('reverse')
	if request.GET.get('reverse') == "true":
		reverse = "false"
		sorted_products = Product.objects.order_by('-name')		
	else:
		reverse = "true"
		sorted_products = Product.objects.order_by('name')
	return render(request, "products/products.html",  {"products": sorted_products, "reverse": reverse})


def sort_prod_price(request):
	#Code!
	sorted_products = Product.objects.order_by('price')		
	return render(request, "products/products.html",  {"products": sorted_products})


def filtered_cat(request):
	print request.GET.get('pd')
	cat_filter = request.GET.get('pd')
	print cat_filter
	filtered_category = Product.objects.filter(category=cat_filter)		
	print filtered_category
	return render(request, "products/products.html",  {"products": filtered_category})


