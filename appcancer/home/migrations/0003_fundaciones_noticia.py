# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctores_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=150)),
                ('cuentabancaria', models.IntegerField()),
                ('numerotelefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('titulo', models.IntegerField()),
                ('cotenido', models.IntegerField()),
                ('imagen', models.CharField(max_length=100)),
                ('fechapublicacion', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
