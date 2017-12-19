# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Product

# Register your models here.
#admin.site.register(Product)

# Reformatting output on product display to make basic product management easier for site admin
class ProductAdmin(admin.ModelAdmin):
	list_filter = ('category', 'stock_level')
	list_display = ('name', 'description', 'price')


	def get_actions(self, request):
		#Disable delete
		actions = super(ProductAdmin, self).get_actions(request)
		del actions['delete_selected']
		return actions

	def has_delete_permission(self, request, obj=None):
		#Disable delete
		return False

# Register the admin class with the associated model
admin.site.register(Product, ProductAdmin)
