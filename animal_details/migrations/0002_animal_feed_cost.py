# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='Feed_cost',
            field=models.FloatField(default=0),
        ),
    ]