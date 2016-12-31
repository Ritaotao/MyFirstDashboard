# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0023_remove_nodsplit_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodsplit',
            name='Update',
            field=models.ForeignKey(blank=True, to='membership.Update', null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='update',
            field=models.ForeignKey(blank=True, to='membership.Update', null=True),
        ),
    ]
