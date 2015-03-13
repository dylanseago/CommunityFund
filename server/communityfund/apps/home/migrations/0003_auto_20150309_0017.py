# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150309_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='community',
            field=models.ForeignKey(to='home.Community', related_name='projects'),
            # preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='initiator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='initiated'),
            # preserve_default=True,
        ),
    ]
