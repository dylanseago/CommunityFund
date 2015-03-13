# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20150309_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('amount', models.PositiveIntegerField()),
                ('funded_on', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(related_name='fundings', to='home.Project')),
                ('user', models.ForeignKey(related_name='fundings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='project',
            old_name='time_to_fund',
            new_name='deadline',
        ),
        migrations.RemoveField(
            model_name='project',
            name='amount_funded',
        ),
    ]
