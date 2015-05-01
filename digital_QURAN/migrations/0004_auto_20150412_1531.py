# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import digital_QURAN.models


class Migration(migrations.Migration):

    dependencies = [
        ('digital_QURAN', '0003_QURAN-TEXT_insertion'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuranTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=255)),
                ('translator', models.CharField(max_length=255)),
                ('language_flag_img', models.FileField(upload_to=digital_QURAN.models.language_flag_image)),
                ('translation_file', models.FileField(upload_to=digital_QURAN.models.translation_file)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '9 - Quran Translation',
                'verbose_name_plural': '9 - Quran Translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuranTranslationText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sura', models.IntegerField()),
                ('aya', models.IntegerField()),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('tranlation', models.ForeignKey(to='digital_QURAN.QuranTranslation')),
            ],
            options={
                'verbose_name': '10 - Quran Translation Text',
                'verbose_name_plural': '10 - Quran Translation Text',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='hizb',
            options={'verbose_name': '3 - Hizb __ META-DATA', 'verbose_name_plural': '3 - Hizb __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='juz',
            options={'verbose_name': '1- Juz __ META-DATA', 'verbose_name_plural': '1- Juz __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='manzil',
            options={'verbose_name': '4 - Manzil __ META-DATA', 'verbose_name_plural': '4 - Manzil __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': '6 - Page __ META-DATA', 'verbose_name_plural': '6 - Page __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='qurantext',
            options={'verbose_name': '8 - Quran Text', 'verbose_name_plural': '8 - Quran Text'},
        ),
        migrations.AlterModelOptions(
            name='ruku',
            options={'verbose_name': '5 - Ruku __ META-DATA', 'verbose_name_plural': '5 - Ruku __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='sajda',
            options={'verbose_name': '7 - Sajda __ META-DATA', 'verbose_name_plural': '7 - Sajda __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='sura',
            options={'verbose_name': '2 - Sura __ META-DATA', 'verbose_name_plural': '2 - Sura __ META-DATA'},
        ),
    ]
