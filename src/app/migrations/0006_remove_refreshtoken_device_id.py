# Generated by Django 4.1.7 on 2023-04-27 03:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_refreshtoken_jti"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="refreshtoken",
            name="device_id",
        ),
    ]
