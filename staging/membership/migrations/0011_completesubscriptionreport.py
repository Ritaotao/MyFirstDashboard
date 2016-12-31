# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0010_delete_completesubscriptionreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteSubscriptionReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_id', models.IntegerField(default=None)),
                ('status', models.CharField(max_length=100, blank=True)),
                ('lst_ord_date', models.DateTimeField(null=True, blank=True)),
                ('nxt_ord_date', models.DateField(null=True, blank=True)),
                ('interval', models.CharField(max_length=200, blank=True)),
                ('exp_date', models.DateField(null=True, blank=True)),
                ('cust_id', models.IntegerField(null=True, blank=True)),
                ('mage_cust_id', models.IntegerField(null=True, blank=True)),
                ('first', models.CharField(max_length=200, blank=True)),
                ('last', models.CharField(max_length=200, blank=True)),
                ('email', models.CharField(max_length=200, blank=True)),
                ('prod_id', models.IntegerField(null=True, blank=True)),
                ('prod_name', models.CharField(max_length=200, blank=True)),
                ('sku', models.CharField(max_length=200, blank=True)),
                ('price', models.DecimalField(max_digits=12, decimal_places=4, blank=True)),
                ('discount', models.DecimalField(max_digits=12, decimal_places=4, blank=True)),
                ('qty', models.IntegerField(default=0)),
                ('ship_method', models.CharField(max_length=200, blank=True)),
                ('mage_bill_addy', models.IntegerField(null=True, blank=True)),
                ('mage_ship_addy', models.IntegerField(null=True, blank=True)),
                ('payment_token', models.IntegerField(null=True, blank=True)),
                ('coupon', models.CharField(max_length=200, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
