# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
  name = models.CharField(max_length=100, default="None")	

class OrderItem(models.Model):
  order_date = models.DateTimeField(auto_now_add=True)
  order = models.ForeignKey('orders.Order')
  product = models.ForeignKey('products.Product')
  quantity = models.IntegerField(default=0)
  price = models.IntegerField(default=0)
  customer = models.ForeignKey('accounts.user') 
  address_line1 = models.CharField(max_length=100, default="None")
  address_line2 = models.CharField(max_length=100, default="None")
  county = models.CharField(max_length=100, default="None")
  postcode = models.CharField(max_length=100, default="None")

