# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last_name')),
                ('telephone', models.CharField(max_length=10, verbose_name='telephone')),
            ],
        ),
    ]
