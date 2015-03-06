# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20150301_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='initiator',
            field=models.ForeignKey(to='search.User'),
            # preserve_default=True,
        ),
    ]
