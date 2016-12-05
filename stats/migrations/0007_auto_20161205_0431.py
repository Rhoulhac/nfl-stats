# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_auto_20161205_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='quaterback',
            name='interceptions',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='quaterback',
            name='touchdowns',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(choices=[('GA', 'Georgia'), ('TX', 'Texas'), ('FL', 'Florida'), ('MO', 'Missouri'), ('MN', 'Minnesota')], max_length=4),
        ),
    ]
