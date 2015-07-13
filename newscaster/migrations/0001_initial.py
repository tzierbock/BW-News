# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('slug', models.CharField(max_length=600, verbose_name=b'Slug')),
                ('raw_body', models.TextField(help_text=b'Unmodified input text', verbose_name=b'Raw Text')),
                ('content', models.TextField(help_text=b'XHTML of compiled markdown', null=True, verbose_name=b'Content', blank=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
