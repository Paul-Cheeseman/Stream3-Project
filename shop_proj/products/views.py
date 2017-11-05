# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product
from django.db.models import Q


# Create your views here.


#Change to list all 
def all_products(request):
	products = Product.objects.all()
	return render(request, "products/products.html", {"products": products})







def basket_add(request):
	product = request.POST['product']
	amount = request.POST['amount']	

 	cart = request.session.get('cart', {})
 	#print product
 	#print amount

 	if int(amount) == 0:
 		print "zero val"
 		#remove from cart
 		if product in cart:
			cart.pop(product)
			request.session['cart'] = cart
			#print cart 
 	else: 
 		cart[product] = amount
		request.session['cart'] = cart

	print "cart info:"
	print request.session['cart']
	products = Product.objects.all()
	return render(request, "products/products.html", {"products": products})






def basket_rem(request):
	#print request.POST['product']
	product = request.POST['product']
	print "product to remove:"
	print product
	count = 0
	basket_item = {}

	#Dodgey coding
	text_str = ""

 	basket = request.session.get('cart', {})
 	print "Basket:"
	print basket


	if product in basket:
		basket.pop(product)
		request.session['cart'] = basket
		#print cart 

	#is basket empty after item removed?
	# empty dictionary returns false

	if basket:
		print "in basket"
		for item_key in basket:
			print "basket item"
			print item_key
 			print basket[item_key]
 			print "-----------------"
 		#query_add = query_add + ""
			basket_item[count] = Product.objects.filter(id=item_key)

			if count == 0:
 				text_str = "products = basket_item[%d]" %(count)

			else:
				text_str = text_str + " | basket_item[%d]" %(count)

	 		#print text_str
			count += 1

		#print "text_str"		
		#print text_str
		#Dodgey coding
		exec text_str

	 	#exec(products)
		#print products
		print "something in"
		return render(request, "products/basket.html", {"products": products})
	else:
		print "nothing in"
		return render(request, "products/basket.html")





def basket_list(request):

	prod_item = {}
	products = {}
	count = 0
	
	#Dodgey coding?
	text_str = ""

	#print "cart"
	#print request.session.get('cart', {})
 	basket = request.session.get('cart', {})
	print basket

	for item_key in basket:

		#print "basket item"
		#print item_key
 		#print basket[item_key]

 		#query_add = query_add + ""

 		prod_item[count] = Product.objects.filter(id=item_key)



 		if count == 0:
 			text_str = "products = prod_item[%d]" %(count)

 		else:
 			text_str = text_str + " | prod_item[%d]" %(count)

 		#print text_str
 		count += 1

 	#Dodgey coding
 	exec text_str


	#print products


 	#print products
 	#pulling out product object where product is equal to name, adding quantity?

	#for item in basket:
		#print item, cart[item] 
	#	print item	
	#	print Product.objects.get(id=basket[item])

	return render(request, "products/basket.html", {"products": products})






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


