# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20170117_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='modelnumber',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='locomotive',
            name='modelnumber',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='locomotive',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
