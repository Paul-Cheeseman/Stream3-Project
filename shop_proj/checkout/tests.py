from django.core.urlresolvers import resolve
from django.test import TestCase

from checkout.views import checkout

class CheckoutBasicTests(TestCase):
	#Check URL resolves to correct view
	def test_checkout_page_resolves(self):
		checkout_res = resolve('/checkout')
		self.assertEqual(checkout_res.func, checkout)

