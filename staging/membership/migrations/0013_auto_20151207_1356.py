# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0012_auto_20151207_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completesubscription',
            name='discount',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscription',
            name='price',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True),
        ),
    ]
