# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20171120_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address_line1',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='address_line2',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='county',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='postcode',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
