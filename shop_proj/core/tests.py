# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.utils import timezone
from django.test.client import RequestFactory

from accounts.models import User
from accounts.views import login



# Create your tests here.

class AccountsTest(TestCase):
 
	def setUp(self):
		super(AccountsTest, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

#Need to put in when PROFILE.html has a home
	def test_profile_page_logged_in_content(self):
		self.client.login(username='testing@account.com', password='testing')
		home_page = self.client.get('/core/profile/')
		home_page_template_output = render_to_response("profile.html", {'user': self.user}).content
		self.assertEquals(home_page.content, home_page_template_output)




	def test_profile_page_logged_in_content(self):
		self.client.login(username='testing@account.com', password='testing')
        home_page = self.client.get('/')
         home_page_template_output = render_to_response("index.html", {'user': self.user}).content
        self.assertEquals(home_page.content, home_page_template_output)
