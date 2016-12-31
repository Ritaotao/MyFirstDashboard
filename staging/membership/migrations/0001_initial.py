# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_id', models.IntegerField(default=None)),
                ('status', models.CharField(max_length=200)),
                ('lst_ord_date', models.DateTimeField()),
                ('nxt_ord_date', models.DateField()),
                ('interval', models.CharField(max_length=200)),
                ('exp_date', models.DateField()),
                ('cust_id', models.IntegerField()),
                ('mage_cust_id', models.IntegerField()),
                ('first', models.CharField(max_length=200)),
                ('last', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('prod_id', models.IntegerField()),
                ('prod_name', models.CharField(max_length=200)),
                ('sku', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=12, decimal_places=4)),
                ('discount', models.DecimalField(max_digits=12, decimal_places=4)),
                ('qty', models.IntegerField(default=0)),
                ('ship_method', models.CharField(max_length=200)),
                ('mage_bill_addy', models.IntegerField()),
                ('mage_ship_addy', models.IntegerField()),
                ('payment_token', models.IntegerField()),
                ('coupon', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
        ),
    ]
