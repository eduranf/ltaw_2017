# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_auto_20170318_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='price',
            new_name='price_euros',
        ),
        migrations.RenameField(
            model_name='cd',
            old_name='price',
            new_name='price_euros',
        ),
    ]
