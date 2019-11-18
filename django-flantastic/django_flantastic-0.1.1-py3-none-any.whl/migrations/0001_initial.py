# Generated by Django 2.2.7 on 2019-11-14 15:17

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bakerie",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("enseigne", models.CharField(max_length=256)),
                ("codpos", models.CharField(blank=True, max_length=8)),
                ("commune", models.CharField(blank=True, max_length=256)),
                ("siren", models.BigIntegerField(null=True)),
                ("vmaj", models.CharField(default=None, max_length=256, null=True)),
                ("vmaj1", models.CharField(default=None, max_length=256, null=True)),
                ("vmaj2", models.CharField(default=None, max_length=256, null=True)),
                ("vmaj3", models.CharField(default=None, max_length=256, null=True)),
                ("datemaj", models.CharField(default=None, max_length=256, null=True)),
                ("modified_date", models.DateTimeField(auto_now=True, null=True)),
                (
                    "global_note",
                    models.PositiveSmallIntegerField(
                        default=None,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("geom", django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "gout",
                    models.PositiveSmallIntegerField(
                        default=None,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "pate",
                    models.PositiveSmallIntegerField(
                        default=None,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "texture",
                    models.PositiveSmallIntegerField(
                        default=None,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "apparence",
                    models.PositiveSmallIntegerField(
                        default=None,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("commentaire", models.CharField(blank=True, max_length=500)),
                ("modified_date", models.DateTimeField(auto_now=True, null=True)),
                (
                    "bakerie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flantastic.Bakerie",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
