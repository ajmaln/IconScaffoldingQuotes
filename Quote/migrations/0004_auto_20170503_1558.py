# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0003_item_hiring_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='hiring_days',
            field=models.IntegerField(null=True),
        ),
    ]
