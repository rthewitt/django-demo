# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jump',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('exit_altitude', models.DecimalField(blank=True, decimal_places=1, default=12.5, max_digits=4)),
                ('pull_altitude', models.DecimalField(blank=True, decimal_places=1, default=4.5, max_digits=3)),
                ('notes', models.TextField()),
                ('aircraft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logbook.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='Parachute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook.Container')),
                ('main_canopy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='logbook.Parachute')),
                ('reserve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='logbook.Parachute')),
            ],
        ),
        migrations.AddField(
            model_name='jump',
            name='equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logbook.Rig'),
        ),
    ]
