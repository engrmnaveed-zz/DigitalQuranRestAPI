# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital_QURAN', '0007_auto_20150420_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecitationPageByPage',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('language', models.CharField(max_length=45)),
                ('translator', models.CharField(max_length=255)),
                ('quality_Kbps', models.IntegerField(help_text=b'Interger Value, eg: for 64 Kbps just enter 64')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '4.0- Quran Recitation Page-By-Page',
                'verbose_name_plural': '4.0- Quran Recitation Page-By-Page',
            },
            bases=(models.Model,),
        ),
    ]
