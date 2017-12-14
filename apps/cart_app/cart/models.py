# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from products.models import Product

# Create your models here.



class Cart(models.Model):
	name = models.CharField(max_length=100)

	#To get applicable cart object out of database
	@classmethod
	def get_cart(cls, cart_id):
		cart = Cart.objects.get(id=cart_id)
		return cart

	#Creates the link between the cart model created in the database to 
	#the value stored in the session variable to reference the cart
	def create_cart(self, request):
		self.save()
		request['cart'] = self.id	


	#Check if the cart has ANY items in it
	def items_in_cart(self):
		cart_queryset = CartItem.objects.filter(cart_id=self)
		if cart_queryset.exists():
			return cart_queryset

	#Check if the cart has a specific item in it
	def item_in_cart(self, product_id):
		cart_queryset = CartItem.objects.filter(cart_id=self, product_id=product_id)
		if cart_queryset.exists():
			return cart_queryset


	def update_cart(self, product_id, amount):
		#prevent risk of error if called on empty cart
		if int(amount) == 0:
			self.remove_from_cart(product_id)

		else:
			if self.items_in_cart():
				cart_queryset = self.items_in_cart()
				for item in cart_queryset:
					if item.product_id == int(product_id):
						print("updating item in cart")
						item.amount = amount
						item.save()		


	def add_to_cart(self, product_id, amount):
		print("new item for cart")
		product_to_add = Product.objects.get(id=product_id)
		cart = Cart.objects.get(id=self.id)
		cartItem = CartItem(cart=cart, product=product_to_add, amount=amount)
		cartItem.save()


	def remove_from_cart(self, product_id):
		#prevent risk of error if called on empty cart
		print("Remove from Cart")
		if self.items_in_cart():
			cart_queryset = CartItem.objects.filter(cart_id=self.id)
			for item in cart_queryset:
				if item.product_id == int(product_id):
					CartItem.objects.filter(id=item.id).delete()



	def add_quantity(self):
		print("Add Quantity")
		if self.items_in_cart():
			cart_queryset = self.items_in_cart()

			#for each cart item, use the stored product_id to retrieve product details from product table
			products = Product.objects.filter(id__in=[item.product_id for item in cart_queryset])

			#getting amount ordered of each product so can auto-fill cart list
			for item in products:
				cartItem_amount = CartItem.objects.get(product_id=item.id, cart_id=self.id)
				item.amount = cartItem_amount.amount

			return products


	def list_cart(self, product_id):
		print("")


	def del_cart(self, request):

		#remove all cart items from db
		items_in_cart = CartItem.objects.filter(cart_id=self.id)
		for item in items_in_cart:
			CartItem.objects.filter(id=item.id).delete()

		#remove cart from db
		Cart.objects.filter(id=self.id).delete()		

		#delete session key
		del request.session['cart']





class CartItem(models.Model):
	cart = models.ForeignKey('cart.Cart')
	product = models.ForeignKey('products.Product')
	amount = models.IntegerField(default=0)





