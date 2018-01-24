# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response

from core.views import get_profile, get_index, get_services, get_contact

class CoreTest(TestCase):

	#Testing URL resolution
	def test_index_page_view(self):
		index_page = resolve('/')
		self.assertEqual(index_page.func, get_index)

	#Testing URL resolution
	def test_profile_page_view(self):
		profile_page = resolve('/core/profile/')
		self.assertEqual(profile_page.func, get_profile)

	#Testing URL resolution
	def test_services_page_view(self):
		services_page = resolve('/core/services/')
		self.assertEqual(services_page.func, get_services)

	#Testing URL resolution
	def test_contact_page_view(self):
		contact_page = resolve('/core/contact/')
		self.assertEqual(contact_page.func, get_contact)

	#Testing Page Content
	def test_index_page_content(self):
		index_page = self.client.get('/')
		index_page_template_output = render_to_response("index.html").content
		self.assertEquals(index_page.content, index_page_template_output)

	#Testing Page Content
	def test_profile_page_content(self):
		profile_page = self.client.get('/core/profile/')
		profile_page_template_output = render_to_response("profile.html").content
		self.assertEquals(profile_page.content, profile_page_template_output)

	#Testing Page Content
	def test_services_content(self):
		services_page = self.client.get('/core/services/')
		services_page_template_output = render_to_response("services.html").content
		self.assertEquals(services_page.content, services_page_template_output)

	#Testing Page Content
	def test_contact_page_content(self):
		contact_page = self.client.get('/core/contact/')
		contact_page_template_output = render_to_response("contact.html").content
		self.assertEquals(contact_page.content, contact_page_template_output)
