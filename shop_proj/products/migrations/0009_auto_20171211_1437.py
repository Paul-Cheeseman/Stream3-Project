# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20171107_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.CharField(default='X', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.CharField(default='None', max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='xxx', max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_alt',
            field=models.CharField(default='img alt', max_length=20),
        ),
    ]
