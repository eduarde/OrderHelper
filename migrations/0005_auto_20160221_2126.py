# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderhelper', '0004_auto_20160221_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persoana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100, verbose_name='Nume')),
                ('prenume', models.CharField(max_length=100, verbose_name='Prenume')),
                ('telefon', models.CharField(max_length=10, verbose_name='Telefon')),
            ],
        ),
        migrations.RenameModel(
            old_name='Project',
            new_name='Proiect',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RenameField(
            model_name='proiect',
            old_name='description',
            new_name='descriere',
        ),
        migrations.RenameField(
            model_name='proiect',
            old_name='telephone',
            new_name='telefon',
        ),
        migrations.RenameField(
            model_name='proiect',
            old_name='title',
            new_name='titlu',
        ),
    ]
