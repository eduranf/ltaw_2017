# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0025_auto_20170319_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='video',
            field=models.FileField(upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='cd',
            name='audio',
            field=models.FileField(upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='cd',
            name='cover',
            field=models.FileField(upload_to=b'products'),
        ),
    ]
