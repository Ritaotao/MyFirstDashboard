# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0024_auto_20151215_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nodsplit',
            old_name='Update',
            new_name='update',
        ),
    ]
