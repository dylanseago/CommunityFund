# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uID', models.IntegerField(serialize=False, primary_key=True)),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('rating', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.AlterField(
            model_name='project',
            name='pID',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='initiator',
            field=models.ForeignKey(to='search.User', to_field=b'uID'),
        ),
    ]
