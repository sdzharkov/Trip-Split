# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-13 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripapp', '0005_auto_20161110_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]