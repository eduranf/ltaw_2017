# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0014_cd_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cd',
            old_name='audio',
            new_name='Track',
        ),
    ]
