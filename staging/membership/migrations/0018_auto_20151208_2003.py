# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0017_update_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='avg_additional_churn',
            field=models.DecimalField(default=0.075, max_digits=8, decimal_places=4),
        ),
        migrations.AddField(
            model_name='update',
            name='buffer',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='update',
            name='new_gift_member',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='update',
            name='new_member',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='update',
            name='r2w1_percent',
            field=models.DecimalField(default=0.6, max_digits=6, decimal_places=4),
        ),
    ]
