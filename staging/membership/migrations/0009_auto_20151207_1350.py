# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20151207_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='coupon',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='discount',
            field=models.DecimalField(max_digits=12, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='email',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='first',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='interval',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='last',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='mage_bill_addy',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='mage_ship_addy',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='payment_token',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='price',
            field=models.DecimalField(max_digits=12, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='prod_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='ship_method',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='sku',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='status',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
