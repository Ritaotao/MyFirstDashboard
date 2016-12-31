# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_auto_20151207_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='coupon',
            field=models.CharField(default=b' ', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='created',
            field=models.DateTimeField(default=b' ', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='email',
            field=models.CharField(default=b' ', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='exp_date',
            field=models.DateField(default=b' ', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='first',
            field=models.CharField(default=b' ', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='interval',
            field=models.CharField(default=b' ', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='last',
            field=models.CharField(default=b' ', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='lst_ord_date',
            field=models.DateTimeField(default=b' ', blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='nxt_ord_date',
            field=models.DateField(default=b' ', blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='prod_name',
            field=models.CharField(default=b' ', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='ship_method',
            field=models.CharField(default=b' ', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='sku',
            field=models.CharField(default=b' ', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='status',
            field=models.CharField(default=b' ', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='updated',
            field=models.DateTimeField(default=b' ', null=True, blank=True),
        ),
    ]
