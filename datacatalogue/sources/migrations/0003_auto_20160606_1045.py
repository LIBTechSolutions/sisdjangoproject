# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0002_auto_20160605_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='maintainer_email',
        ),
        migrations.RemoveField(
            model_name='source',
            name='maintainer_phone',
        ),
        migrations.AlterField(
            model_name='source',
            name='access_method',
            field=models.CharField(choices=[('HTTP GET', 'HTTP GET'), ('HTTP POST', 'HTTP POST'), ('FTP', 'FTP'), ('SFTP', 'SFTP'), ('GOOGLE DRIVE', 'GOOGLE DRIVE'), ('S3', 'S3'), ('EMAIL', 'EMAIL')], default=' ', max_length=30, verbose_name='Description of access protocol'),
        ),
        migrations.AlterField(
            model_name='source',
            name='availability',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], default=' ', max_length=30, null=True, verbose_name='Last known availability'),
        ),
        migrations.AlterField(
            model_name='source',
            name='encoding',
            field=models.CharField(choices=[('UTF-8', 'UTF-8'), ('US-ASCII', 'US-ASCII'), ('UTF-16', 'UTF-16'), ('UTF-32', 'UTF-32')], default=' ', max_length=30, verbose_name='Character encoding (e.g. UTF-8)'),
        ),
        migrations.AlterField(
            model_name='source',
            name='encryption',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True, verbose_name='Name / link to encryption algorithm used'),
        ),
        migrations.AlterField(
            model_name='source',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Arabic', 'Arabic'), ('French', 'French'), ('German', 'German'), ('Portuguese', 'Portuguese'), ('Spanish', 'Spanish')], default=' ', max_length=30, verbose_name='Language in which the data is written'),
        ),
        migrations.AlterField(
            model_name='source',
            name='pii',
            field=models.BooleanField(default=False, verbose_name='Does source contain personally-identifiable information?'),
        ),
        migrations.AlterField(
            model_name='source',
            name='regex',
            field=models.TextField(blank=True, default=' ', max_length=30, null=True, verbose_name='RegEx expression used with access method'),
        ),
        migrations.AlterField(
            model_name='source',
            name='system_of_record',
            field=models.BooleanField(default=False, max_length=30, verbose_name='Is this is a primary resource? (i.e. not a replica or extract)'),
        ),
    ]
