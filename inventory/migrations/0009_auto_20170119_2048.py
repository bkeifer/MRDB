# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20170119_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locomotive',
            name='address',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locomotive',
            name='axles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locomotive',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locomotive',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
