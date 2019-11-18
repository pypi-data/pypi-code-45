# Generated by Django 2.0.13 on 2019-03-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("notifications", "0003_auto_20190319_1048")]

    operations = [
        migrations.AlterField(
            model_name="notificationsconfig",
            name="api_root",
            field=models.URLField(
                default="https://ref.tst.vng.cloud/nc/api/v1",
                unique=True,
                verbose_name="api root",
            ),
        )
    ]
