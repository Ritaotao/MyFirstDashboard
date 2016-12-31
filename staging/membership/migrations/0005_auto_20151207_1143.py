# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_auto_20151207_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='coupon',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='created',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='cust_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='discount',
            field=models.DecimalField(default=None, max_digits=12, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='email',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='exp_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='first',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='interval',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='last',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='lst_ord_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='mage_bill_addy',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='mage_cust_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='mage_ship_addy',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='nxt_ord_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='payment_token',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='price',
            field=models.DecimalField(default=None, max_digits=12, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='prod_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='prod_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='ship_method',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='sku',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='status',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='completesubscriptionreport',
            name='updated',
            field=models.DateTimeField(default=None),
        ),
    ]
