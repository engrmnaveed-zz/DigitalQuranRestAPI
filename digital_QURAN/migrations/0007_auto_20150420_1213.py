# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital_QURAN', '0006_recitationversebyverse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recitationversebyverse',
            name='quality_Kbps',
            field=models.IntegerField(help_text=b'Interger Value, eg: for 64 Kbps just enter 64'),
            preserve_default=True,
        ),
    ]
