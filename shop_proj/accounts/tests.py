# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.utils import timezone
from django.test.client import RequestFactory
from django import forms
from .forms import UserRegistrationForm, UserLoginForm
from accounts.models import User
from accounts.views import login, logout, user_register



# Create your tests here.

class AccountsPageTest(TestCase):
	def setUp(self):
		super(AccountsPageTest, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

	#Testing URL resolution
	def test_login_page_view(self):
		login_page = resolve('/accounts/login/')
		self.assertEqual(login_page.func, login)

	#Testing URL resolution
	def test_logout_page_view(self):
		logout_page = resolve('/accounts/logout/')
		self.assertEqual(logout_page.func, logout)

	#Testing URL resolution
	def test_user_reg_page_view(self):
		user_register_page = resolve('/accounts/user_register/')
		self.assertEqual(user_register_page.func, user_register)



 
class AccountsFormsTest(TestCase):
	#Based on code from Code Institute
	def test_registration_form(self):
		form = UserRegistrationForm({
			'email': 'testing@account.com',
			'password1': 'testing',
			'password2': 'testing',
		})
		self.assertTrue(form.is_valid())


	#Based on code from Code Institute
	def test_registration_form_fails_with_missing_email(self):
		form = UserRegistrationForm({
			'password1': 'testing',
			'password2': 'testing',
		})
		self.assertFalse(form.is_valid())
		self.assertRaisesMessage(forms.ValidationError,"Please enter your email address", form.full_clean())


	#Based on code from Code Institute
	def test_registration_form_fails_with_incorrect_password(self):
		form = UserRegistrationForm({
			'email': 'testing@account.com',			
			'password1': 'testing',
			'password2': 'wrong',
		})
		self.assertFalse(form.is_valid())
		self.assertRaisesMessage(forms.ValidationError,"Passwords do not match", form.full_clean())
