# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20170316_1608'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bikes',
            new_name='Bike',
        ),
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='CDs',
            new_name='CD',
        ),
    ]
