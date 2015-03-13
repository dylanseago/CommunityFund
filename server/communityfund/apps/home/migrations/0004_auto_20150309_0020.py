# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150309_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='creator',
            field=models.ForeignKey(related_name='communities_created', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='community',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscriptions', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='initiator',
            field=models.ForeignKey(related_name='projects_created', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
