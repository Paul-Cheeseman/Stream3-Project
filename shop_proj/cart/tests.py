# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response

from cart.models import Cart
from products.models import Product
from cart.views import cart_add, cart_list 

# Create your tests here.
 
class CartPageTests(TestCase):

    #Check URL resolves to correct view
	def test_cart_list_page_resolves(self):
		list_cart_res = resolve('/cart_list')
		self.assertEqual(list_cart_res.func, cart_list)

	#Check URL resolves to correct view
	def test_cart_add_page_resolves(self):
		add_cart_res = resolve('/cart_add')
		self.assertEqual(add_cart_res.func, cart_add)

	#Check URL returns a page (not a page not found etc)
	def test_cart_list_page_status_code_is_ok(self):
		list_cart_status = self.client.get('/cart_list')
		self.assertEqual(list_cart_status.status_code, 200)

	#Check URL returns a page (not a page not found etc)
	def test_cart_add_page_status_code_is_ok(self):
		add_cart_status = self.client.get('/cart_add')
		self.assertEqual(add_cart_status.status_code, 200)

	#Check page content
	def test_cart_list_check_content_is_correct(self):
		#Checking the right template is used
		list_cart_template = self.client.get('/cart_list')
		self.assertTemplateUsed(list_cart_template, "cart/cart.html")
		#Checking content of the template is correct
		list_cart_template_output = render_to_response("cart/cart.html").content
		self.assertEqual(list_cart_template.content, list_cart_template_output)
		
	#Check page content
	def test_cart_add_check_content_is_correct(self):
		#Checking the right template is used
		add_cart_template = self.client.get('/cart_add/')
		self.assertTemplateUsed(add_cart_template, "products/products.html")
		#Checking content of the template is correct
		add_cart_template_output = render_to_response("products/products.html").content
		self.assertEqual(add_cart_template.content, add_cart_template_output)



class CartPageUnitTests(TestCase):
	
	#fixtures = ['products']

	print("test test")
	print(Product.objects.all())




