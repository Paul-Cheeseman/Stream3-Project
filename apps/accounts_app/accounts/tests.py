# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.utils import timezone
from django.test.client import RequestFactory


from accounts.models import User
from accounts.views import login, register_cc



# Create your tests here.

class AccountsTest(TestCase):
 
	def setUp(self):
		super(AccountsTest, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

	def test_login_page_view(self):
		login_page = resolve('/login/')
		self.assertEqual(login_page.func, login)

	def test_register_page_view(self):
		login_page = resolve('/register_cc/')
		self.assertEqual(login_page.func, register_cc)


	def test_profile_page_logged_in_content(self):
		self.client.login(username='testing@account.com', password='testing')
		home_page = self.client.get('/profile/')
		home_page_template_output = render_to_response("profile.html", {'user': self.user}).content
		self.assertEquals(home_page.content, home_page_template_output)





