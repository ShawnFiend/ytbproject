# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 04:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album',
            new_name='album_title',
        ),
    ]
