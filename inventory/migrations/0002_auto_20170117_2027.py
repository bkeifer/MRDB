# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='railroad',
            name='mark',
            field=models.CharField(default='X', max_length=5),
            preserve_default=False,
        ),
    ]
