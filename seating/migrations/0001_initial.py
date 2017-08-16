# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0021_auto_20161008_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col', models.IntegerField()),
                ('row', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SeatingRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision_number', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=1024)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventPage')),
            ],
        ),
        migrations.CreateModel(
            name='SeatingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_rows', models.IntegerField()),
                ('max_cols', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='revision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seating.SeatingRevision'),
        ),
        migrations.AddField(
            model_name='seat',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='seatingrevision',
            unique_together=set([('event', 'revision_number')]),
        ),
    ]
