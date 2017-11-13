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


		# -------------------------------------
		# If posted value is 0, remove from cart
		# -------------------------------------
		

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
		#del request.session['cart']


	#if cart not exist
		#create and add product
	#else
		#add product

	return render(request, "cart/cart.html")
	#return render(request, "cart/cart.html", {"products": products})




#Change to list all 
def cart_list(request):

	print("Cart id:")
	print(request.session['cart'])

	if 'cart' in request.session:
		
		#Select all records from Cart_Item for current id
		items_in_cart = CartItem.objects.filter(cart_id=request.session['cart'])		

		#for each cart item, use the stored product_id to retrive product details from product table
		products = Product.objects.filter(id__in=[item.product_id for item in items_in_cart])


		return render(request, "cart/cart.html", {"products": products})

	#MAYBE A DIFFERENT TEMPLATE or use "MESSAGE" to put message at top??
	return render(request, "cart/cart.html")




#remove from cart

#list cart
