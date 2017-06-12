# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='cover_path',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shortvideo',
            name='file_path',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shortvideo',
            name='preview_path',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='torrent',
            name='torrent_path',
            field=models.CharField(max_length=100, null=True),
        ),
    ]