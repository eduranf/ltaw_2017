# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20170316_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='vid',
            new_name='video',
        ),
    ]
