# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-10 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_productinbusket'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbusket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
