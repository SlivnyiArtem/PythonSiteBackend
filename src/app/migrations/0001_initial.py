# Generated by Django 4.1.7 on 2023-05-15 04:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="email address")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="BankingAccount",
            fields=[
                ("account_number", models.IntegerField(primary_key=True, serialize=False)),
                ("currency_amount", models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name="SimpleUser",
            fields=[
                ("simple_user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("full_username", models.CharField(max_length=255, null=True)),
                ("user_name", models.CharField(max_length=255)),
                ("surname", models.CharField(max_length=255)),
                ("phone_number", models.BigIntegerField(blank=True, null=True)),
                ("hash_of_password", models.CharField(blank=True, default=None, max_length=255, null=True)),
                ("login_access", models.BooleanField(default=True)),
                ("friends", models.ManyToManyField(blank=True, related_name="f", to="app.simpleuser")),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.DecimalField(decimal_places=2, max_digits=20)),
                ("transaction_date", models.DateField(null=True)),
                (
                    "transaction_recipient",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="recipients",
                        to="app.simpleuser",
                    ),
                ),
                (
                    "transaction_sender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="senders",
                        to="app.simpleuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RefreshToken",
            fields=[
                ("Jti", models.CharField(max_length=10000, primary_key=True, serialize=False)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.simpleuser")),
            ],
        ),
        migrations.CreateModel(
            name="Card",
            fields=[
                ("card_number", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "MM",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(12),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("YY", models.IntegerField()),
                ("system", models.CharField(max_length=20)),
                (
                    "banking_account",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="app.bankingaccount"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bankingaccount",
            name="account_owner",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="app.simpleuser"),
        ),
    ]
