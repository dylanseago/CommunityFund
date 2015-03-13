# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20150305_2150'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
