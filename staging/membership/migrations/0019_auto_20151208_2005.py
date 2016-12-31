# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0018_auto_20151208_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='update',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
