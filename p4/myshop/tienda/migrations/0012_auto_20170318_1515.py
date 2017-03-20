# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0011_auto_20170318_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='topic',
            field=models.CharField(max_length=40),
        ),
    ]
