from django.test import TestCase

from django.conf import settings
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response
from django.test import TestCase
from django.utils import timezone

from accounts.models import User
from orders.views import orders_list, orders_detail


class OrdersPageTests(TestCase):

	#Create user in test database for authentication testing
	def setUp(self):
		super(OrdersPageTests, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

	#Testing URL resolves to correct page
	def test_orders_list_page_view(self):
		orders_list_page = resolve('/orders/list/')
		self.assertEqual(orders_list_page.func, orders_list)

	#Testing URL resolves to correct page
	def test_orders_detail_page_view(self):
		orders_detail_page = resolve('/orders/detail/')
		self.assertEqual(orders_detail_page.func, orders_detail)

	#Check that unauthorised users get denied and redirected from orders list page
	def test_orders_list_redirect_works(self):
		orders_list_response = self.client.get('/orders/list/')	
		self.assertEqual(orders_list_response.status_code, 302)
		self.assertRedirects(orders_list_response, "{0}?next={1}".format(settings.LOGIN_URL, reverse(orders_list)))

	#Check that authorised users can access to orders list page
	def test_orders_list_authorised_users(self):
		self.client.login(username='testing@account.com', password='testing')
		orders_list_response = self.client.get('/orders/list/')	
		self.assertEqual(orders_list_response.status_code, 200)

	#Check that unauthorised users get denied and redirected from orders detail page
	def test_orders_detail_redirect_works(self):
		orders_detail_response = self.client.get('/orders/detail/')	
		self.assertEqual(orders_detail_response.status_code, 302)
		self.assertRedirects(orders_detail_response, "{0}?next={1}".format(settings.LOGIN_URL, reverse(orders_detail)))

	#Check that authorised users can access to orders detail page
	def test_orders_detail_authorised_users(self):
		self.client.login(username='testing@account.com', password='testing')
		orders_detail_response = self.client.get('/orders/detail/')	
		self.assertEqual(orders_detail_response.status_code, 200)
