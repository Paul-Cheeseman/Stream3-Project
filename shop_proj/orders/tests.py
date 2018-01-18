from django.test import TestCase

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase

from orders.views import orders_list, orders_detail


class OrdersPageTests(TestCase):
	#Testing URL resolution
	def test_orders_list_page_view(self):
		orders_list_page = resolve('/orders/list/')
		self.assertEqual(orders_list_page.func, orders_list)

	#Testing URL resolution
	def test_orders_detail_page_view(self):
		orders_detail_page = resolve('/orders/detail/')
		self.assertEqual(orders_detail_page.func, orders_detail)
