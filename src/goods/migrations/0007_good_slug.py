# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-22 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20170812_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='slug',
            field=models.SlugField(max_length=50, blank=True, null=True),
        ),
    ]