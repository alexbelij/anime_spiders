# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-16 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0007_add_cg_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cg',
            name='pixiv_id',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='cg',
            name='source',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]
