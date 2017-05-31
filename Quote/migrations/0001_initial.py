# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('unit_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('attention', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('site', models.CharField(max_length=100)),
                ('total', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quote.Quote'),
        ),
    ]
