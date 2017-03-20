# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0020_auto_20170319_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='genre',
            field=models.CharField(max_length=40),
        ),
    ]
