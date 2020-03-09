# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2020-03-09 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectorassignment', '0003_auto_20200308_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='continent',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='country',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
