# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[(b'Dog', b'Dog'), (b'Cat', b'Cat')], default=b'Dog', max_length=40, verbose_name=b'Type'),
        ),
    ]
