# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org_manager', '0003_auto_20160201_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizations',
            name='org_level',
        ),
        migrations.RemoveField(
            model_name='organizations',
            name='org_powers',
        ),
        migrations.AddField(
            model_name='organizations',
            name='org_level_223',
            field=models.CharField(blank=True, default=b'', max_length=1000),
        ),
        migrations.AddField(
            model_name='organizations',
            name='org_level_44',
            field=models.CharField(blank=True, default=b'', max_length=1000),
        ),
        migrations.AddField(
            model_name='organizations',
            name='org_powers_223',
            field=models.CharField(blank=True, default=b'', max_length=1000),
        ),
        migrations.AddField(
            model_name='organizations',
            name='org_powers_44',
            field=models.CharField(blank=True, default=b'', max_length=1000),
        ),
    ]
