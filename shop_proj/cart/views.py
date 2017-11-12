# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from products.models import Product
from cart.models import Cart, CartItem



#Change to list all 
def cart_add(request):

	if 'cart' not in request.session:

		print("no cart found")
		cart = Cart()
		#create cart in db
		cart.save()
		request.session['cart'] = cart.id

		print("cart id")
		print(cart.id)

		#testing element
		#this is be accessed via the POST value
		test_product = Product.objects.get(id=1)


		cartItem = CartItem(cart=cart, product=test_product, amount=1)
		cartItem.save()

	else:
		print("cart found")
		#print("cart found")

		#testing element
		#this is be accessed via the POST value
		test_product = Product.objects.get(id=2)
		print("test product")
		print(test_product.name)

		print ("cart session value")
		print(request.session['cart'])

		cart = Cart.objects.get(id=request.session['cart'])

		cartItem = CartItem(cart=cart, product=test_product, amount=2)
		
		cartItem.save()

		#This is testing, put this at checkout and logout
		del request.session['cart']


	#if cart not exist
		#create and add product
	#else
		#add product

	return render(request, "cart/cart.html")
	#return render(request, "cart/cart.html", {"products": products})




#Change to list all 
def list_cart(request):
	#code!

	#------------------------------------------------
	#product2 = Product.objects.filter(id=2)
	product2 = Product.objects.get(id=2)
	print (product2.id)
	print (product2.category)


	#products = 
	#cartthing = CartItem(cart=testcart, product=product2)	
	#print(cartthing.product.name)
	#------------------------------------------------

	return render(request, "cart/cart.html", {"products": products})


#add to cart
	#Test for Cart
    	#create new cart instance

    	#update with new product!

    	#create in database

    	#update session variable with cart_id from db


#remove from cart

#list cart
