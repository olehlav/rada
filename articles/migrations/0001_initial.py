# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('sport', 'спорт'), ('news', 'новини'), ('advert', 'оголошення'), ('school', 'школа'), ('holiday', 'свято'), ('etc', 'різне')], max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('univiews', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to=None, blank=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
