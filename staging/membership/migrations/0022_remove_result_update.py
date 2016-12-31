# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0021_auto_20151214_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='update',
        ),
    ]
