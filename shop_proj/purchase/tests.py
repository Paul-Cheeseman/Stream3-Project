	# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render_to_response
from django.test import TestCase
from django.utils import timezone

from accounts.models import User
from purchase.views import address, register_cc
from .forms import CCRegistrationForm, AddressForm


class PurchasePageTests(TestCase):

	#Create user in test database for authentication testing
	def setUp(self):
		super(PurchasePageTests, self).setUp()
		self.user = User.objects.create(username='testing@account.com')
		self.user.set_password('testing')
		self.user.last_login = timezone.now()
		self.user.save()

	#Testing URL resolves to correct page
	def test_address_form_page_view(self):
		address_form_page = resolve('/purchase/address/')
		self.assertEqual(address_form_page.func, address)

	#Testing URL resolves to correct page
	def test_cc_form_page_view(self):
		cc_form_page = resolve('/purchase/register_cc/')
		self.assertEqual(cc_form_page.func, register_cc)

	#Check that unauthorised users get denied and redirected from cc_reg page
	def test_cc_form_redirect_works(self):
		cc_reg_response = self.client.get('/purchase/register_cc/')	
		self.assertEqual(cc_reg_response.status_code, 302)
		self.assertRedirects(cc_reg_response, "{0}?next={1}".format(settings.LOGIN_URL, reverse(register_cc)))

	#Check that unauthorised users get denied and redirected from address page
	def test_address_redirect_works(self):
		address_response = self.client.get('/purchase/address/')	
		self.assertEqual(address_response.status_code, 302)
		self.assertRedirects(address_response, "{0}?next={1}".format(settings.LOGIN_URL, reverse(address)))

	#Check that authorised users can access to cc_reg page
	def test_cc_form_authorised_users(self):
		self.client.login(username='testing@account.com', password='testing')
		cc_reg_response = self.client.get('/purchase/register_cc/')	
		self.assertEqual(cc_reg_response.status_code, 200)

	#Check that authorised users can access to address page
	def test_address_authorised_users(self):
		self.client.login(username='testing@account.com', password='testing')		
		address_response = self.client.get('/purchase/address/')	
		self.assertEqual(address_response.status_code, 200)


class PurchaseCCRegFormTest(TestCase):
	#Based on code from Code Institute
	def test_cc_registration_form(self):
		form = CCRegistrationForm({
			'stripe_id': settings.STRIPE_TEST_TOKEN,
			'credit_card_number': 4242424242424242,
			'cvv': 123,
			'expiry_month': 1,
			'expiry_year': 2033
		})
		self.assertTrue(form.is_valid())


class PurchaseAddressFormTest(TestCase):
 	#Address form completed correctly, should be valid
	def test_address_form(self):
		form = AddressForm({
			'address_line1': '45 Test Street',
			'address_line2': 'Long Test Lane',
			'county': 'Testville',
			'postcode': 'TE00 0ST'
		})
		self.assertTrue(form.is_valid())

	#Address shouldn't allow non alpanumeric's (except spaces)
	def test_address_line1_non_alphaNu(self):
		form = AddressForm({
			'address_line1': '*',
			'address_line2': 'Long Test Lane',
			'county': 'Testville',
			'postcode': 'TE00 0ST'
		})
		self.assertFalse(form.is_valid())

	#Address shouldn't allow non alpanumeric's (except spaces)
	def test_address_line2_non_alphaNu(self):
		form = AddressForm({
			'address_line1': '45 Test Street',			
			'address_line2': '*',
			'county': 'Testville',
			'postcode': 'TE00 0ST'
		})
		self.assertFalse(form.is_valid())

	#Postcode shouldn't allow non alpanumeric's (except spaces)
	def test_county_non_alphaNu(self):
		form = AddressForm({
			'address_line1': '45 Test Street',			
			'address_line2': 'Long Test Lane',
			'county': '*',
			'postcode': 'TE00 0ST'
		})
		self.assertFalse(form.is_valid())

	#Postcode should have max 8 chars
	def test_postcode_8_chars(self):
		form = AddressForm({
			'address_line1': '45 Test Street',			
			'address_line2': 'Long Test Lane',
			'county': 'Testville',
			'postcode': 'AA11 1AA'
		})
		self.assertTrue(form.is_valid())

	#Postcode should have max 7 chars
	def test_postcode_7_chars(self):
		form = AddressForm({
			'address_line1': '45 Test Street',			
			'address_line2': 'Long Test Lane',
			'county': 'Testville',
			'postcode': 'AA111AA'
		})
		self.assertTrue(form.is_valid())

	#Postcode should have max 8 chars, this has 9
	def test_postcode_too_long(self):
		form = AddressForm({
			'address_line1': '45 Test Street',			
			'address_line2': 'Long Test Lane',
			'county': 'Testville',
			'postcode': 'AA11 1AAA'
		})
		self.assertFalse(form.is_valid())
		self.assertRaisesMessage(forms.ValidationError,"Please enter a valid postcode", form.full_clean())

	#Postcode should have min 7 chars, this has 6
	def test_postcode_too_short(self):
		form = AddressForm({
			'address_line1': '45 Test Street',			
			'address_line2': 'Long Test Lane',
			'county': 'Testville',
			'postcode': 'AA111A'
		})
		self.assertFalse(form.is_valid())
		self.assertRaisesMessage(forms.ValidationError,"Please enter a valid postcode", form.full_clean())	
