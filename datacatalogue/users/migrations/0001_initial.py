# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name of contact')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name of contact')),
                ('email_address', models.EmailField(max_length=254, verbose_name='E-mail address of contact')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number of contact')),
            ],
        ),
        migrations.CreateModel(
            name='LDAP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc', models.CharField(default='DC=', max_length=100, verbose_name='LDAP domainComponent (DC)')),
                ('ou', models.CharField(default='OU=', max_length=100, verbose_name='LDAP organizationalUnitName (OU)')),
                ('o', models.CharField(default='O=', max_length=100, verbose_name='LDAP organizationalName (O)')),
                ('l', models.CharField(default='L=', max_length=100, verbose_name='LDAP localityName (L)')),
                ('street', models.CharField(default='ST=', max_length=100, verbose_name='LDAP stateOrProvinceName (ST)')),
                ('cn', models.CharField(default='C=', max_length=100, verbose_name='LDAP countryName(C)')),
                ('uid', models.CharField(default='UID=', max_length=100, verbose_name='LDAP userId (UID)')),
                ('dn', models.CharField(default='DN=', max_length=255, verbose_name='LDAP distinguishedName (DN)')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='limited', max_length=100, verbose_name='Scope (used by view service)')),
                ('url', models.CharField(max_length=256, verbose_name='Tenant home page')),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Contact')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='ldap_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.LDAP'),
        ),
    ]
