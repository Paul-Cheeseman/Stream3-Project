from django.core.urlresolvers import resolve, reverse
from django.conf import settings
from django.test import TestCase
from django.utils import timezone

from checkout.views import checkout
from accounts.models import User

class CheckoutBasicTests(TestCase):
	
	#Create user in test database for authentication testing
	def setUp(self):
		super(CheckoutBasicTests, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

	#Check URL resolves to correct view
	def test_checkout_page_resolves(self):
		checkout_res = resolve('/checkout')
		self.assertEqual(checkout_res.func, checkout)

	#Check that authorised users can access to page
	def test_checkout_page_authorised_users(self):
		self.client.login(username='testing@account.com', password='testing')
		checkout_response = self.client.get('/checkout')	
		self.assertEqual(checkout_response.status_code, 200)

	#Check that unauthorised users get denied and redirected from page
	def test_checkout_redirect_works(self):
		checkout_response = self.client.get('/checkout')	
		self.assertEqual(checkout_response.status_code, 302)
		self.assertRedirects(checkout_response, "{0}?next={1}".format(settings.LOGIN_URL, reverse(checkout)))

