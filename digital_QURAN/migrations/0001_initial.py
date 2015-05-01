# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hizb',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Hizb',
                'verbose_name_plural': 'Hizb',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Juz',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Juz',
                'verbose_name_plural': 'Juz',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manzil',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Manzil',
                'verbose_name_plural': 'Manzil',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Page',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuranText',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'QuranText',
                'verbose_name_plural': 'QuranText',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ruku',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Ruku',
                'verbose_name_plural': 'Ruku',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sajda',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('type', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Sajda',
                'verbose_name_plural': 'Sajda',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sura',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('ayas', models.IntegerField()),
                ('start', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('tname', models.CharField(max_length=255)),
                ('ename', models.CharField(max_length=255)),
                ('type', models.CharField(default=b'Meccan', max_length=45, choices=[(b'Meccan', b'Meccan'), (b'Medinan', b'Medinan')])),
                ('order', models.IntegerField()),
                ('rukus', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Sura',
                'verbose_name_plural': 'Sura',
            },
            bases=(models.Model,),
        ),
    ]
