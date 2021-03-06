# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 16:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20160917_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='finish',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 17, 17, 27, 20, 664293)),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='signup_freshers_open',
            field=models.DateTimeField(blank=True, help_text='Set a date for when freshers may sign up to the event, leave blank if they are to sign up at the                   same time as everyone else', null=True),
        ),
    ]
