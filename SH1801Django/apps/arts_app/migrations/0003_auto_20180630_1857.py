# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-30 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts_app', '0002_auto_20180630_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='phone',
            field=models.IntegerField(default=0, verbose_name='订单配送电话'),
        ),
    ]
