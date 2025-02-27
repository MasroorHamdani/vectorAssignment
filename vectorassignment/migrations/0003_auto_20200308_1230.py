# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2020-03-08 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vectorassignment', '0002_auto_20200308_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='no_of_roads',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='no_of_schools',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='no_of_shops',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='no_of_trees',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='continent',
            name='area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='continent',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='no_of_hospital',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='no_of_nationalparks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='no_of_rivers',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='no_of_schools',
            field=models.IntegerField(),
        ),
    ]
