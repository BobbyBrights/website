# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_forum', '0003_auto_20171007_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='is_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='is_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
