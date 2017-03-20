# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0023_auto_20170319_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(upload_to=b'tienda/products/bikes'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='video',
            field=models.FileField(upload_to=b'tienda/products/bikes'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to=b'tienda/products/books'),
        ),
        migrations.AlterField(
            model_name='cd',
            name='audio',
            field=models.FileField(upload_to=b'tienda/products/cds'),
        ),
        migrations.AlterField(
            model_name='cd',
            name='cover',
            field=models.FileField(upload_to=b'tienda/products/cds'),
        ),
    ]
