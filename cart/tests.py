# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase

from cart.models import Cart, CartItem
from products.models import Product
from cart.views import cart_add, cart_list 

# Create your tests here.


class CartPageTests(TestCase):

    #Check URL resolves to correct view
	def test_cart_list_page_resolves(self):
		list_cart_res = resolve('/cart/cart_list')
		self.assertEqual(list_cart_res.func, cart_list)

	#Check URL resolves to correct view
	def test_cart_add_page_resolves(self):
		add_cart_res = resolve('/cart/cart_add')
		self.assertEqual(add_cart_res.func, cart_add)

	#Check URL returns a page (not a page not found etc)
	def test_cart_list_page_status_code_is_ok(self):
		list_cart_status = self.client.get('/cart/cart_list')
		self.assertEqual(list_cart_status.status_code, 200)

	#Check URL returns a page (not a page not found etc)
	def test_cart_add_page_status_code_is_ok(self):
		add_cart_status = self.client.get('/cart/cart_add')
		self.assertEqual(add_cart_status.status_code, 200)



class CartUnitTests(TestCase):

	def setUp(self):
		#Product id in test database will be descending, 1, 2, 3 etc
		Product.objects.create(name = "Test Prod1", description = "Test Prod1", size = "Small", gender = "Male", age = "Adult", colour = "Red", price = 3.99, stock_level = 10, category = "T-Shirts", photo = "Test-photo.jpg", photo_alt = "Test-photo alt")
		Product.objects.create(name = "Test Prod2", description = "Test Prod2", size = "Small", gender = "Male", age = "Adult", colour = "Blue", price = 3.99, stock_level = 10, category = "T-Shirts", photo = "Test-photo.jpg", photo_alt = "Test-photo alt")
		Product.objects.create(name = "Test Prod3", description = "Test Prod3", size = "Small", gender = "Male", age = "Adult", colour = "Yellow", price = 3.99, stock_level = 10, category = "T-Shirts", photo = "Test-photo.jpg", photo_alt = "Test-photo alt")
		Cart.objects.create(id=101)

	
	def test_getCart(self):
		Cart.objects.create(id=1)
		self.assertEqual(Cart.get_cart(1).id, 1)

	def test_getCart_willFail(self):
		Cart.objects.create(id=1)
		self.assertNotEqual(Cart.get_cart(1).id, 2)


	#How many individual items in cart
	def test_items_in_cart_with_contents(self):
		cart = Cart.get_cart(101)
		#Adding two products to cart
		cart.add_to_cart(1, 1)
		cart.add_to_cart(2, 1)		
		function_queryset = cart.items_in_cart()
		self.assertEqual(function_queryset.count(), 2)

	#How many individual items in cart
	def test_items_in_cart_no_contents(self):
		cart = Cart.get_cart(101)
		function_queryset = cart.items_in_cart()
		self.assertEqual(None, function_queryset)


	#The accumlative total of all item order quantities in cart
	#Each item has been ordered in a quantity of 3, so total of 9
	def test_amount_items_in_cart(self):
		cart = Cart.get_cart(101)
		cart.add_to_cart(1, 3)
		cart.add_to_cart(2, 3)
		cart.add_to_cart(3, 3)
		self.assertEqual(cart.amount_items_in_cart(), 9)

	#The accumlative total of all item order quantities in cart, empty cart.
	def test_amount_items_in_cart_empty_cart(self):
		cart = Cart.get_cart(101)
		self.assertEqual(cart.amount_items_in_cart(), 0)


	#Add two items to cart
	def test_add_to_cart(self):
		cart = Cart.get_cart(101)
		cart.add_to_cart(1, 1)
		cart.add_to_cart(2, 1)		
		amount_in_cart = CartItem.objects.filter(cart_id=101).count()
		self.assertEqual(amount_in_cart, 2)

	#Add item to cart, increase amount from 1 to 5
	def test_update_cart_amount_increase(self):
		cart = Cart.get_cart(101)
		cart.add_to_cart(1, 1)
		cart.update_cart(1, 5)
		amount_in_cart = CartItem.objects.get(cart_id=101, product_id=1).amount
		self.assertEqual(amount_in_cart, 5)

	#Add item to cart, reduce amount from 3 to 1
	def test_update_cart_amount_decrease(self):
		cart = Cart.get_cart(101)
		cart.add_to_cart(1, 3)
		cart.update_cart(1, 1)
		amount_in_cart = CartItem.objects.get(cart_id=101, product_id=1).amount
		self.assertEqual(amount_in_cart, 1)

	#Add two items to cart, then remove one by updating with an amount of zero
	def test_update_cart_item_remove(self):
		cart = Cart.get_cart(101)
		cart.add_to_cart(1, 3)		
		cart.add_to_cart(2, 2)		
		cart.update_cart(1, 0)
		amount_in_cart = CartItem.objects.filter(cart_id=101).count()
		self.assertEqual(amount_in_cart, 1)

	#Add two items to cart, then remove one using function and product
	def test_remove_from_cart(self):
		cart = Cart.get_cart(101)
		cart.add_to_cart(1, 3)		
		cart.add_to_cart(2, 2)		
		cart.remove_from_cart(1)
		amount_in_cart = CartItem.objects.filter(cart_id=101).count()
		self.assertEqual(amount_in_cart, 1)
