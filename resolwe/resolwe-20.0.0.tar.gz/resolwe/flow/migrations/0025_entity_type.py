# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-07 08:44
from __future__ import unicode_literals

from django.db import migrations


def populate_entity_type(apps, schema_editor):
    """Populate entity type from attached descriptor schema."""
    Entity = apps.get_model('flow', 'Entity')

    for entity in Entity.objects.all():
        if entity.descriptor_schema is not None:
            entity.type = entity.descriptor_schema.slug
            entity.save()


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0024_process_entity_3'),
    ]

    operations = [
        migrations.RunPython(populate_entity_type)
    ]
