# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.utils import timezone
from django.test.client import RequestFactory


from purchase.views import address, register_cc


# Create your tests here.
class AccountsTest(TestCase):
 
	def setUp(self):
		super(AccountsTest, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

	def test_cc_register_page_view(self):
		register_cc = resolve('/register_cc/')
		self.assertEqual(register_cc, register_cc)







