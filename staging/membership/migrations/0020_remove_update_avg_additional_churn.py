# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0019_auto_20151208_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='avg_additional_churn',
        ),
    ]
