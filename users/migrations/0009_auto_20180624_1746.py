# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-24 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_useractionlog_action_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractionlog',
            name='action',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='useractionlog',
            name='action_data',
            field=models.CharField(default='', max_length=256),
        ),
    ]
