# Generated by Django 4.1.7 on 2023-04-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_rename_jti_authtoken_jti"),
    ]

    operations = [
        migrations.AddField(
            model_name="simpleuser",
            name="login_access",
            field=models.BooleanField(default=False),
        ),
    ]