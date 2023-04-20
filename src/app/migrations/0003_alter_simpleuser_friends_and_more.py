# Generated by Django 4.1.7 on 2023-04-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_simpleuser_friends_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="simpleuser",
            name="friends",
            field=models.ManyToManyField(blank=True, related_name="f", to="app.simpleuser"),
        ),
        migrations.AlterField(
            model_name="simpleuser",
            name="transactions_history",
            field=models.ManyToManyField(blank=True, to="app.transactionlog"),
        ),
    ]
