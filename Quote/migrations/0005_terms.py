# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0004_auto_20170503_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.TextField(max_length=5000)),
            ],
        ),
    ]
