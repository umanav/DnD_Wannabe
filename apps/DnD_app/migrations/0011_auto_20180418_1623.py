# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-18 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DnD_app', '0010_game_strength'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='strength',
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
