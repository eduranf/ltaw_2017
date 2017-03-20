# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20170316_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='bike_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='bike_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='bike_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='bike_model',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='bike_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='bike_units',
            new_name='units',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='bike_vid',
            new_name='vid',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_topic',
            new_name='topic',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_units',
            new_name='units',
        ),
        migrations.RenameField(
            model_name='cd',
            old_name='CD_album',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='cd',
            old_name='CD_artist',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='cd',
            old_name='CD_audio',
            new_name='audio',
        ),
        migrations.RenameField(
            model_name='cd',
            old_name='CD_genre',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='cd',
            old_name='CD_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='cd',
            old_name='CD_units',
            new_name='units',
        ),
    ]
