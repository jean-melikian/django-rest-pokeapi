# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 08:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0008_auto_20170610_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 11, 8, 29, 43, 346184, tzinfo=utc)),
        ),
    ]
