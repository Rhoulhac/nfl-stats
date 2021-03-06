# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_auto_20161205_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(choices=[('GA', 'Georgia'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('TX', 'Texas'), ('FL', 'Florida')], max_length=4),
        ),
        migrations.AlterField(
            model_name='quaterback',
            name='interceptions',
            field=models.IntegerField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='quaterback',
            name='touchdowns',
            field=models.IntegerField(max_length=2, null=True),
        ),
    ]
