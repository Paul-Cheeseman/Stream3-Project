# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20171107_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo_alt',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
