# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import TestCase

from products.views import products, product_detail


class ProductPageTests(TestCase):
	#Testing URL resolution
	def test_product_list_page_view(self):
		product_list_page = resolve('/products/list/')
		self.assertEqual(product_list_page.func, products)

	#Testing URL resolution
	def test_product_detail_page_view(self):
		product_detail_page = resolve('/products/detail/')
		self.assertEqual(product_detail_page.func, product_detail)


