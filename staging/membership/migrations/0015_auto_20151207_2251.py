# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0014_auto_20151207_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completesubscription',
            name='payment_token',
            field=models.CharField(default=' ', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
