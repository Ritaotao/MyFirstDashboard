# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0020_remove_update_avg_additional_churn'),
    ]

    operations = [
        migrations.CreateModel(
            name='NODSplit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField()),
                ('left', models.DateField()),
                ('ng_red3_l', models.IntegerField()),
                ('ng_white3_l', models.IntegerField()),
                ('ng_variety3_l', models.IntegerField()),
                ('ng_red6_l', models.IntegerField()),
                ('ng_white6_l', models.IntegerField()),
                ('ng_variety6_l', models.IntegerField()),
                ('g_red3_l', models.IntegerField()),
                ('g_white3_l', models.IntegerField()),
                ('g_variety3_l', models.IntegerField()),
                ('right', models.DateField()),
                ('end', models.DateField()),
                ('ng_red3_r', models.IntegerField()),
                ('ng_white3_r', models.IntegerField()),
                ('ng_variety3_r', models.IntegerField()),
                ('ng_red6_r', models.IntegerField()),
                ('ng_white6_r', models.IntegerField()),
                ('ng_variety6_r', models.IntegerField()),
                ('g_red3_r', models.IntegerField()),
                ('g_white3_r', models.IntegerField()),
                ('g_variety3_r', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('fm_churn', models.DecimalField(max_digits=12, decimal_places=4)),
                ('nfm_churn', models.DecimalField(max_digits=12, decimal_places=4)),
                ('pop_ng', models.IntegerField()),
                ('pop_gi', models.IntegerField()),
                ('bot_red', models.IntegerField()),
                ('bot_white', models.IntegerField()),
                ('red_perc', models.DecimalField(max_digits=12, decimal_places=4)),
                ('white_perc', models.DecimalField(max_digits=12, decimal_places=4)),
                ('pop_3pack', models.IntegerField()),
                ('pop_6pack', models.IntegerField()),
                ('wa', models.DecimalField(verbose_name=b'weighted_average', max_digits=12, decimal_places=4)),
                ('tot_pack', models.IntegerField()),
                ('tot_bottles', models.IntegerField()),
                ('red_bottles', models.IntegerField()),
                ('white_bottles', models.IntegerField()),
                ('tot_cases', models.IntegerField()),
                ('red_cases', models.IntegerField()),
                ('white_cases', models.IntegerField()),
                ('reds_each', models.IntegerField()),
                ('whites_each', models.IntegerField()),
                ('update', models.ForeignKey(to='membership.Update')),
            ],
        ),
        migrations.AddField(
            model_name='nodsplit',
            name='result',
            field=models.ForeignKey(to='membership.Result'),
        ),
    ]
