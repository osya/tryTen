# pylint: disable=C0103
# Generated by Django 2.0.2 on 2018-02-26 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180224_1431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={
                'ordering': ('-price', 'name'),
                'verbose_name': 'good',
                'verbose_name_plural': 'goods'
            },
        ),
    ]
