# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20170804_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='menumodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]