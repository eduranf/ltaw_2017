# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_auto_20170318_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='color',
            field=models.CharField(max_length=30),
        ),
    ]
