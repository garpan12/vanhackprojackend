# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160306_0939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sos',
            old_name='sos_user',
            new_name='user_uuid',
        ),
        migrations.AlterField(
            model_name='sos',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
