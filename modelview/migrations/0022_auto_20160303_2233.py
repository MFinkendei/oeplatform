# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelview', '0021_auto_20160303_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energymodel',
            name='model_file_format',
            field=models.CharField(choices=[('.exe', '.exe'), ('.gms', '.gms'), ('.py', '.py'), ('.xls', '.xls'), ('other', 'other')], default='other', help_text='In which format is the model saved?', max_length=5, verbose_name='Model file format'),
        ),
        migrations.AlterField(
            model_name='energymodel',
            name='model_input',
            field=models.CharField(choices=[('.csv', '.csv'), ('.py', '.py'), ('text', 'text'), ('.xls', '.xls'), ('other', 'other')], default='other', help_text='Of which file format are the input and output data?', max_length=5, verbose_name='Input/output data file format'),
        ),
    ]