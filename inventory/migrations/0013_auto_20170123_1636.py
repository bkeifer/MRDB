# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20170123_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='coupler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Coupler'),
        ),
        migrations.AlterField(
            model_name='locomotive',
            name='coupler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Coupler'),
        ),
    ]
