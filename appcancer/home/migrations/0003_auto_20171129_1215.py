# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 12:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_doctores_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_doc', models.CharField(default='nombre_doc', max_length=100)),
                ('apellidopat_doc', models.CharField(default='apellido_doc', max_length=100)),
                ('apellidomat_doc', models.CharField(default='apellido_doc', max_length=100)),
                ('titulos', models.TextField()),
                ('cedulatitulacion', models.CharField(max_length=100)),
                ('Doctor_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=50, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_profile',
            },
        ),
        migrations.RemoveField(
            model_name='doctores',
            name='Doctor_user',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Nombre',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='codigopostal',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='telefono',
            field=models.IntegerField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Doctores',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='doctor',
            name='idFundacion_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Hospital'),
        ),
    ]