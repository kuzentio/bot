# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0015_auto_20170705_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paddypowerbet',
            name='uniid',
        ),
        migrations.AlterField(
            model_name='race',
            name='horses',
            field=models.ManyToManyField(blank=True, related_name='races', to='scraper.Horse'),
        ),
    ]