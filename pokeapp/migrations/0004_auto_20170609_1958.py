# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 17:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0003_auto_20170609_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 10, 17, 58, 46, 319789, tzinfo=utc)),
        ),
    ]