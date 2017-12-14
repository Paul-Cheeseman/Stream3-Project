# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
  customer = models.ForeignKey('accounts.user') 
  address_line1 = models.CharField(max_length=100, default="None")
  address_line2 = models.CharField(max_length=100, default="None")
  county = models.CharField(max_length=100, default="None")
  postcode = models.CharField(max_length=100, default="None")
  order_date = models.DateTimeField(auto_now_add=True)
  total = models.DecimalField(max_digits=6, decimal_places=2)

  class Meta:
    ordering = ['order_date']

class OrderItem(models.Model):
  order = models.ForeignKey('orders.Order')
  product = models.ForeignKey('products.Product')
  quantity = models.IntegerField(default=0)
  price = models.IntegerField(default=0)


