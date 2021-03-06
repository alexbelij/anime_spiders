# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 06:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import exhibition.models
import filer.fields.file
import filer.fields.image
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('exhibition', '0009_add_cg_tags_and_other_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='filer.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('filer.file',),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='anime',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='cg',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='shortvideo',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='torrent',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='anime',
            name='cover_file',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anime_covers', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='cg',
            name='file',
            field=filer.fields.image.FilerImageField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cgs', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='shortvideo',
            name='preview',
            field=filer.fields.file.FilerFileField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='short_video_previews', to='filer.File'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='desc',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='anime',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.Tagged', to='exhibition.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='cg',
            name='artist_tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedArtists', to='exhibition.Tag', verbose_name='artists'),
        ),
        migrations.AlterField(
            model_name='cg',
            name='character_tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.TaggedCharactors', to='exhibition.Tag', verbose_name='charactors'),
        ),
        migrations.AlterField(
            model_name='cg',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.Tagged', to='exhibition.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='shortvideo',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.Tagged', to='exhibition.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='torrent',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='exhibition.Tagged', to='exhibition.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='shortvideo',
            name='file',
            field=exhibition.models.FilerVideoField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='short_videos', to='exhibition.Video'),
        ),
    ]
