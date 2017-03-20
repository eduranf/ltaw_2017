# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='bike_brand',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='bike_color',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='bike_img',
            field=models.ImageField(upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='bike_model',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='bike_price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='bike_units',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='bike_vid',
            field=models.FileField(upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_image',
            field=models.ImageField(upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_topic',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_units',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cds',
            name='CD_album',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cds',
            name='CD_artist',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cds',
            name='CD_audio',
            field=models.FileField(upload_to=b'products'),
        ),
        migrations.AlterField(
            model_name='cds',
            name='CD_genre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cds',
            name='CD_price',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cds',
            name='CD_units',
            field=models.IntegerField(),
        ),
    ]
