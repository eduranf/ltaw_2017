# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0018_auto_20170318_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cd',
            old_name='Track',
            new_name='audio',
        ),
        migrations.AlterField(
            model_name='cd',
            name='cover',
            field=models.FileField(upload_to=b'products', blank=True),
        ),
    ]
