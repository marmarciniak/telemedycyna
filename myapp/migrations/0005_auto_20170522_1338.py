# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_leki'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leki',
            name='index',
        ),
        migrations.AlterField(
            model_name='leki',
            name='age',
            field=models.IntegerField(blank=True, db_column='Wiek', null=True),
        ),
    ]
