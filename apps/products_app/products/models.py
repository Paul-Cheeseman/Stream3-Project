# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator



# Create your models here.
 
class Product(models.Model):

    SIZES = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    AGE = (
        ('Adult', 'Adult'),
        ('Child', 'Child'),
    )

    COLOUR = (
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),        
        ('Red', 'Red'),
        ('White', 'White'),
        ('Yellow', 'Yellow'),
    )

    CATEGORY = (
        ('T-Shirts', 'T-Shirts'),
        ('Trousers', 'Trousers'),
        ('Shirts', 'Shirts'),
        ('Skirts', 'Skirts'),        
        ('Underwear', 'Underwear'),
    )

    name = models.CharField(max_length=30)
    description = models.TextField()
    size = models.CharField(max_length=6, choices=SIZES)
    gender = models.CharField(max_length=6, choices=GENDER)
    age = models.CharField(max_length=5, choices=AGE)
    colour = models.CharField(max_length=6, choices=COLOUR) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_level = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    category = models.CharField(max_length=30, choices=CATEGORY)
    photo = models.ImageField(upload_to = "img/")
    photo_alt = models.CharField(max_length=20, default="img alt")


    def __str__(self):
        return self.name


