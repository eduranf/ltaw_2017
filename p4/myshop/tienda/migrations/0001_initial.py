# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bike_brand', models.CharField(max_length=20, verbose_name=b'brand')),
                ('bike_model', models.CharField(max_length=20, verbose_name=b'model')),
                ('bike_color', models.CharField(max_length=20, verbose_name=b'color')),
                ('bike_units', models.IntegerField(verbose_name=b'units')),
                ('bike_price', models.DecimalField(verbose_name=b'price', max_digits=6, decimal_places=2)),
                ('bike_vid', models.FileField(upload_to=b'products', verbose_name=b'video')),
                ('bike_img', models.ImageField(upload_to=b'products', verbose_name=b'image')),
                ('pub_date', models.DateTimeField(verbose_name=b'date publised')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_title', models.CharField(max_length=50, verbose_name=b'title')),
                ('book_author', models.CharField(max_length=50, verbose_name=b'author')),
                ('book_topic', models.CharField(max_length=20, verbose_name=b'topic')),
                ('book_units', models.IntegerField(verbose_name=b'units')),
                ('book_price', models.DecimalField(verbose_name=b'price', max_digits=6, decimal_places=2)),
                ('book_image', models.ImageField(upload_to=b'products', verbose_name=b'image')),
                ('pub_date', models.DateTimeField(verbose_name=b'date publised')),
            ],
        ),
        migrations.CreateModel(
            name='CDs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CD_artist', models.CharField(max_length=50, verbose_name=b'artist')),
                ('CD_album', models.CharField(max_length=50, verbose_name=b'album')),
                ('CD_genre', models.CharField(max_length=20, verbose_name=b'genre')),
                ('CD_units', models.IntegerField(verbose_name=b'units')),
                ('CD_price', models.DecimalField(verbose_name=b'price', max_digits=6, decimal_places=2)),
                ('CD_audio', models.FileField(upload_to=b'products', verbose_name=b'audio')),
                ('pub_date', models.DateTimeField(verbose_name=b'date publised')),
            ],
        ),
    ]
