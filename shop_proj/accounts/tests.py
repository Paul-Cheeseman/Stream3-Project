# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response
from django.test import TestCase
from django.utils import timezone
from django import forms

from .forms import UserRegistrationForm, UserLoginForm
from .models import User
from .views import login, logout, user_register


# Create your tests here.
class AccountsPageTest(TestCase):

	#Create user in test database for authentication testing
	def setUp(self):
		super(AccountsPageTest, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

	#Testing URL resolves to correct page
	def test_login_page_view(self):
		login_page = resolve('/accounts/login/')
		self.assertEqual(login_page.func, login)

	#Testing URL resolves to correct page
	def test_logout_page_view(self):
		logout_page = resolve('/accounts/logout/')
		self.assertEqual(logout_page.func, logout)

	#Testing URL resolves to correct page
	def test_user_reg_page_view(self):
		user_register_page = resolve('/accounts/user_register/')
		self.assertEqual(user_register_page.func, user_register)


	#Check that unauthorised users get denied and redirected from logout view
	def test_logout_redirect_works(self):
		logout_response = self.client.get('/accounts/logout/')	
		self.assertEqual(logout_response.status_code, 302)
		self.assertRedirects(logout_response, "{0}?next={1}".format(settings.LOGIN_URL, reverse(logout)))

	#Check that authorised users can access to logout view
	def test_logout_authorised_users(self):
		self.client.login(username='testing@account.com', password='testing')
		logout_response = self.client.get('/accounts/logout/')	
		self.assertRedirects(logout_response, reverse('index'))

 
class AccountsFormsTest(TestCase):

	#Based on code from Code Institute
	def test_registration_form_fails_with_incorrect_password(self):
		form = UserRegistrationForm({
			'email': 'testing@account.com',			
			'password1': 'testing',
			'password2': 'wrong',
		})
		self.assertFalse(form.is_valid())
		self.assertRaisesMessage(forms.ValidationError,"Passwords do not match", form.full_clean())
