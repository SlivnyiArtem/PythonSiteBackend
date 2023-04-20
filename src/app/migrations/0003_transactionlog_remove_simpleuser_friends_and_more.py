# Generated by Django 4.1.7 on 2023-04-20 05:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_simpleuser_full_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransactionLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("transaction_recipient_id", models.IntegerField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=20)),
                ("transaction_date", models.DateField(null=True)),
                ("is_outgoing_transaction", models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name="simpleuser",
            name="friends",
        ),
        migrations.AddField(
            model_name="simpleuser",
            name="transactions_history",
            field=models.ManyToManyField(to="app.transactionlog"),
        ),
        migrations.AddField(
            model_name="simpleuser",
            name="friends",
            field=models.ManyToManyField(related_name="f", to="app.simpleuser"),
        ),
    ]
