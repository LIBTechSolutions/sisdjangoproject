# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-11 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sisdatasources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', multiselectfield.db.fields.MultiSelectField(choices=[('ENGLISH', 'ENGLISH'), ('MATH', 'MATH'), ('HISTORY', 'HISTORY')], default=' ', max_length=5, verbose_name='Subject')),
                ('schedule', multiselectfield.db.fields.MultiSelectField(choices=[('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNESDAY')], default=' ', max_length=5, verbose_name='Teacher Schedule')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sisdatasources.Student')),
            ],
        ),
    ]
