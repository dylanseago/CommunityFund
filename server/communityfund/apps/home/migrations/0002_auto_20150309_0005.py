# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='subscribers',
            field=models.ManyToManyField(related_name='home_community_subscribers', to=settings.AUTH_USER_MODEL),
            # preserve_default=True,
        ),
        migrations.AlterField(
            model_name='community',
            name='creator',
            field=models.ForeignKey(related_name='home_community_creator', to=settings.AUTH_USER_MODEL),
            # preserve_default=True,
        ),
    ]
