# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import digital_QURAN.models


class Migration(migrations.Migration):

    dependencies = [
        ('digital_QURAN', '0004_auto_20150412_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hizb',
            options={'verbose_name': '1.2 - Hizb __ META-DATA', 'verbose_name_plural': '1.2 - Hizb __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='juz',
            options={'verbose_name': '1.0- Juz __ META-DATA', 'verbose_name_plural': '1.0- Juz __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='manzil',
            options={'verbose_name': '1.3 - Manzil __ META-DATA', 'verbose_name_plural': '1.3 - Manzil __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': '1.5 - Page __ META-DATA', 'verbose_name_plural': '1.5 - Page __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='qurantext',
            options={'verbose_name': '2.0 - Quran Text', 'verbose_name_plural': '2.0 - Quran Text'},
        ),
        migrations.AlterModelOptions(
            name='qurantranslation',
            options={'verbose_name': '3.0 - Quran Translation', 'verbose_name_plural': '3.0 - Quran Translation'},
        ),
        migrations.AlterModelOptions(
            name='qurantranslationtext',
            options={'verbose_name': '3.1 - Quran Translation Text', 'verbose_name_plural': '3.1 - Quran Translation Text'},
        ),
        migrations.AlterModelOptions(
            name='ruku',
            options={'verbose_name': '1.4 - Ruku __ META-DATA', 'verbose_name_plural': '1.4 - Ruku __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='sajda',
            options={'verbose_name': '1.6 - Sajda __ META-DATA', 'verbose_name_plural': '1.6 - Sajda __ META-DATA'},
        ),
        migrations.AlterModelOptions(
            name='sura',
            options={'verbose_name': '1.1 - Sura __ META-DATA', 'verbose_name_plural': '1.1 - Sura __ META-DATA'},
        ),
        migrations.AlterField(
            model_name='qurantranslation',
            name='translation_file',
            field=models.FileField(help_text=b'Required : One aya translation per line in format "sura|aya|translation" and file must have all 6236 aya included', upload_to=digital_QURAN.models.translation_file),
            preserve_default=True,
        ),
    ]
