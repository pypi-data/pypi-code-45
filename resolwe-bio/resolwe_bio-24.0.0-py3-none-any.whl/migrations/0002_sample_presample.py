# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-24 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolwe_bio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='presample',
            field=models.BooleanField(default=True),
        ),
    ]
