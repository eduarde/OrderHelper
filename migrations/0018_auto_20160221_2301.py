# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0017_auto_20160221_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcomanda',
            name='data_de_facturare',
            field=models.DateField(blank=True, null=True, verbose_name='Data de facturare'),
        ),
    ]
