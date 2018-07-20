# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('data', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 7, 20, 10, 2, 22, 758681))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 7, 20, 10, 2, 22, 758712))),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
