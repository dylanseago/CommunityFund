# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pID', models.IntegerField()),
                ('initiator', models.IntegerField()),
                ('name', models.TextField()),
                ('goal', models.IntegerField()),
                ('description', models.TextField()),
                ('timeToFund', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
