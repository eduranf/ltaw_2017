# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0019_auto_20170319_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='cover',
            field=models.FileField(upload_to=b'products'),
        ),
    ]
