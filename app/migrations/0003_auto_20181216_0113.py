# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-12-16 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181215_0524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='cool',
        ),
        migrations.RemoveField(
            model_name='review',
            name='funny',
        ),
        migrations.RemoveField(
            model_name='review',
            name='useful',
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.CharField(max_length=50),
        ),
    ]
