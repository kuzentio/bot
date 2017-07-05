# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0013_auto_20170705_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='horses',
            field=models.ManyToManyField(blank=True, null=True, related_name='races', to='scraper.Horse'),
        ),
    ]
