# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20151207_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='coupon',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='cust_id',
            field=models.IntegerField(blank=True),
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
            name='exp_date',
            field=models.DateField(blank=True),
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
            name='lst_ord_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='mage_bill_addy',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='mage_cust_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='mage_ship_addy',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='nxt_ord_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='payment_token',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='price',
            field=models.DecimalField(max_digits=12, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='prod_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='prod_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='qty',
            field=models.IntegerField(default=0, blank=True),
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
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='updated',
            field=models.DateTimeField(blank=True),
        ),
    ]
