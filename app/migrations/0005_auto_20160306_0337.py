# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160306_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sos',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
