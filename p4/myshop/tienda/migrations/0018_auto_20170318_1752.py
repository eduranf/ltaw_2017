# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0017_auto_20170318_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='cover',
            field=models.FileField(upload_to=b'products'),
        ),
    ]
