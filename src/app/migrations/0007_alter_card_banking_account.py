# Generated by Django 4.1.7 on 2023-03-14 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_card_card_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='banking_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bankingaccount'),
        ),
    ]
