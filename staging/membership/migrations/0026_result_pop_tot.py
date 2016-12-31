# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0025_auto_20151215_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='pop_tot',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
