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

from django.test import Client


class CheckoutBasicTests(TestCase):
	#Check URL resolves to correct view
	def test_checkout_page_resolves(self):
		checkout_res = resolve('/checkout')
		self.assertEqual(checkout_res.func, checkout)

