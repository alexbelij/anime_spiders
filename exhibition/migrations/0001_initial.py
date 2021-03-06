# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawled_from', models.CharField(max_length=100)),
                ('site_pk', models.IntegerField()),
                ('link', models.CharField(max_length=100)),
                ('cover', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('orig_name', models.CharField(max_length=100, null=True)),
                ('pub_date', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawled_from', models.CharField(max_length=100)),
                ('site_pk', models.IntegerField()),
                ('large_file_url', models.CharField(max_length=100)),
                ('file_url', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=300)),
                ('tags_string', models.CharField(max_length=100)),
                ('md5', models.CharField(max_length=100)),
                ('pixiv_id', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShortVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawled_from', models.CharField(max_length=100)),
                ('site_pk', models.IntegerField()),
                ('md5', models.CharField(max_length=100)),
                ('preview_url', models.CharField(max_length=100)),
                ('file_url', models.CharField(max_length=100)),
                ('file_size', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('file_ext', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Torrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crawled_from', models.CharField(max_length=100)),
                ('site_pk', models.IntegerField()),
                ('site', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100, null=True)),
                ('team_id', models.IntegerField(null=True)),
                ('size', models.IntegerField(null=True)),
                ('torrent', models.CharField(max_length=100, null=True)),
                ('magnet', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(null=True)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='torrent',
            unique_together=set([('crawled_from', 'site_pk')]),
        ),
        migrations.AlterUniqueTogether(
            name='shortvideo',
            unique_together=set([('crawled_from', 'site_pk')]),
        ),
        migrations.AlterUniqueTogether(
            name='cg',
            unique_together=set([('crawled_from', 'site_pk')]),
        ),
        migrations.AlterUniqueTogether(
            name='anime',
            unique_together=set([('crawled_from', 'site_pk')]),
        ),
    ]
