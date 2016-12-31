# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0011_completesubscriptionreport'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompleteSubscriptionReport',
            new_name='CompleteSubscription',
        ),
    ]
