# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0009_auto_20151207_1350'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompleteSubscriptionReport',
        ),
    ]
