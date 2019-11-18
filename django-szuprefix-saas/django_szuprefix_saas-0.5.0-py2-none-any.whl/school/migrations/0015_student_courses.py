# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-06 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20180822_2359'),
        ('school', '0014_auto_20180902_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='school_students', to='course.Course', verbose_name='\u8bfe\u7a0b'),
        ),
    ]
