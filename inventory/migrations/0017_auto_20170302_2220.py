# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_carfeature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carfeature',
            name='cars',
            field=models.ManyToManyField(blank=True, to='inventory.Car'),
        ),
    ]
