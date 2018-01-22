from django.core.urlresolvers import resolve
from django.test import TestCase

from checkout.views import checkout

class CheckoutBasicTests(TestCase):
	#Check URL resolves to correct view
	def test_checkout_page_resolves(self):
		checkout_res = resolve('/checkout')
		self.assertEqual(checkout_res.func, checkout)


	def test_checkout_content_is_correct(self):
		checkout = self.client.get('/checkout')	
		print (checkout)
		#self-assertEqual(response.status_code, 302)
		#self-assertRedirect(response, "{0}?next={1}".format()settings.LOGIN_URL, reverse(checkout))

