# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-12-16 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181216_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(),
        ),
    ]
