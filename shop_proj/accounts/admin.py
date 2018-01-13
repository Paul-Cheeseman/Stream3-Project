# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import User

# Define the admin class
# Reformatting output on admin display to make basic user management clearer for site admin
class UserAdmin(admin.ModelAdmin):
   list_display = ('username', 'first_name', 'last_name', 'address_line1', 'address_line2', 'address_line2', 'postcode', 'last_login')

# Register the admin class with the associated model
admin.site.register(User, UserAdmin)