# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-03 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataedit', '0003_remove_tablerevision_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataedit.Schema')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='table',
            name='tags',
            field=models.ManyToManyField(to='dataedit.Tag'),
        ),
        migrations.AddField(
            model_name='schema',
            name='tags',
            field=models.ManyToManyField(to='dataedit.Tag'),
        ),
    ]