# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from products.models import Product

# Create your models here.



class Cart(models.Model):
	name = models.CharField(max_length=100)


class CartItem(models.Model):
  cart = models.ForeignKey('cart.Cart')
  product = models.ForeignKey('products.Product')
  amount = models.IntegerField(default=0)






