# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160305_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address_home',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='emergency_contact',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='secret_code',
            field=models.CharField(max_length=200),
        ),
    ]