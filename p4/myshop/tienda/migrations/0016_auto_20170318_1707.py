# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0015_auto_20170318_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='Track',
            field=models.FileField(default=b'ONE', upload_to=b'products', choices=[(b'ONE', b'ONE'), (b'TWO', b'TWO'), (b'THREE', b'THREE'), (b'FOUR', b'FOUR'), (b'FIVE', b'FIVE'), (b'SIX', b'SIX'), (b'SEVEN', b'SEVEN'), (b'EIGHT', b'EIGHT'), (b'NINE', b'NINE'), (b'TEN', b'TEN'), (b'ELEVEN', b'ELEVEN'), (b'TWELVE', b'TWELVE')]),
        ),
    ]
