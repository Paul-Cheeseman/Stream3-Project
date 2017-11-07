# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product



#Change to list all 
def all_products(request):
	products = Product.objects.all()
	return render(request, "products/products.html", {"products": products})



def basket_add(request):
	#get submitted values
	product = request.POST['product']
	amount = request.POST['amount']	
	cart = request.session.get('cart', {})

	#check to see if user removing via product 
	#page by entering 0 amount
	if int(amount) == 0:
 		print ("zero val")
 		if product in cart:
 			cart.pop(product)
 			request.session['cart'] = cart
	#update the cart
	else:
		print ("something added")
		cart[product] = amount
		request.session['cart'] = cart

	#print "cart info:"
	#print request.session['cart']
	products = Product.objects.all()
	return render(request, "products/products.html", {"products": products})





def basket_rem(request):
	#initialise variables
	count = 0
	basket_item = {}

	#get submitted values
	product = request.POST['product']

	#Dodgey coding? It just gets round an error if not here
	#Create variable before its used
	text_str = ""

	basket = request.session.get('cart', {})

 	#remove the submitted product if it is in the basket
	if product in basket:
		basket.pop(product)
		request.session['cart'] = basket

	#if basket still has items in after product removed
	#build a 
	if basket:
		for item_key in basket:

			#create an individual queryset per item in the basket, then 
			#build string which holds query which merges multiple querysets
			#into a single query set.
			basket_item[count] = Product.objects.filter(id=item_key)

			if count == 0:
 				text_str = "products = basket_item[%d]" %(count)
			else:
				text_str = text_str + " | basket_item[%d]" %(count)

			count += 1

		#Dodgey coding?
		#Changing string to executable code
		exec(text_str)

		return render(request, "products/basket.html", {"products": products})
	else:
		return render(request, "products/basket.html")





def basket_list(request):
	#initialise variables
	basket_item = {}
	products = {}
	count = 0
	#Dodgey coding?
	text_str = ""

	namespace = {}



	basket = request.session.get('cart', {})

	print ("Basket List:")
	print (basket)

 	# I couldn't find a way to create a single queryset using multiple inputs, ie
 	# I couldn't see how I could input  - Products.objects.filter(id=item1_id, id=item2_id, id=item3_id), 
 	# especially for a variable about of items, hence iteration below.
	for item_key in basket:
		#create an individual queryset per item in the basket, then 
		#build string which holds query which merges multiple querysets
		#into a single query set.
		basket_item[count] = Product.objects.filter(id=item_key)

		if count == 0:
			text_str = "products = basket_item[%d]" %(count)
		else:
			text_str = text_str + " | basket_item[%d]" %(count)

		count += 1

		#Dodgey coding?
		#Changing string to executable code
		
	exec(text_str)
	#print(test['text_str'])
	#print(test['products'])
	print(products)

	

	return render(request, "products/basket.html", {"products": products})






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


