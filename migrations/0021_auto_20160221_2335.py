# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0020_auto_20160221_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comanda',
            name='subcomenzi',
        ),
        migrations.RemoveField(
            model_name='subcomanda',
            name='numar_unic_comanda',
        ),
        migrations.AddField(
            model_name='subcomanda',
            name='comanda_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orderhelper.Comanda', verbose_name='Comanda'),
        ),
    ]