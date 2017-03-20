# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_auto_20170316_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='price',
            new_name='price_euros',
        ),
    ]
