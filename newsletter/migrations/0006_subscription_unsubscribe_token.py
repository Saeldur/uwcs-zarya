# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20161009_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='unsubscribe_token',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
