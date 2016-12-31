# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0007_auto_20151207_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='exp_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='lst_ord_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='nxt_ord_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
