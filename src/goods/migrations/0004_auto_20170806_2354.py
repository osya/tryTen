# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 20:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20170806_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='is_stock',
            new_name='in_stock',
        ),
    ]