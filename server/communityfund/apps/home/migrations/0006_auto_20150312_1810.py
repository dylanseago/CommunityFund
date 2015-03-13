# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150312_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='summary',
        ),
    ]
