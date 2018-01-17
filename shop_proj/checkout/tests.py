from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone


from accounts.models import User
from checkout.views import checkout
from cart.models import Cart, CartItem
from products.models import Product


from django.contrib.messages.storage.fallback import FallbackStorage


class CheckoutBasicTests(TestCase):
	def setUp(self):
		super(CheckoutBasicTests, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

		self.client.login(username='testing@account.com', password='testing')

	#Check URL resolves to correct view
	def test_checkout_page_resolves(self):
		checkout_res = resolve('/checkout')
		print(checkout_res)
		self.assertEqual(checkout_res.func, checkout)

'''
	#Check page content is correct
	def test_checkout_content_is_correct(self):
		checkout = self.client.get('/checkout')

		self.assertTemplateUsed(checkout, "checkout/checkout.html")
		checkout_template_output = render_to_response("checkout/checkout.html", {'user': self.user}).content

		print("-----------------------------------------------------------")
		print("First:")		
		print(checkout.content)
		print("-----------------------------------------------------------")
		print("Second:")		
		print(checkout_template_output)
		print("-----------------------------------------------------------")
		self.assertEqual(checkout.content, checkout_template_output)	
'''




