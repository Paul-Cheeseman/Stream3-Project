# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 11:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='address_county',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='address_postcode',
            new_name='postcode',
        ),
    ]