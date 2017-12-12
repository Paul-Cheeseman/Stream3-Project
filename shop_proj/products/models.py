# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm



# Create your models here.
 
class Product(models.Model):
    #made unique so can use a key
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    size = models.CharField(max_length=3, default="xxx") #s, m, l
    gender = models.CharField(max_length=1, default="X") #M or F    
    age = models.CharField(max_length=1, default="X") #A (adult), C (Child)
    colour = models.CharField(max_length=15, default="None") 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_level = models.IntegerField(default=0)
    category = models.CharField(max_length=30)
    photo = models.ImageField(upload_to = "img/")
    photo_alt = models.CharField(max_length=20, default="img alt")



    # Below creates a dictionary of the information needed to 
    # create a paypal button in products.html for the value 'product.paypal_form'
    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }
 
        return PayPalPaymentsForm(initial=paypal_dict)
 
    def __str__(self):
        return self.name


