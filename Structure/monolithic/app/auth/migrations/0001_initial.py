# Generated by Django 3.2.4 on 2022-03-07 14:04

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllowedPhonenumbers",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phonenumber",
                    models.CharField(help_text="bypass phonenumber", max_length=32),
                ),
                ("description", models.CharField(help_text="name", max_length=32)),
            ],
            options={
                "db_table": "mmd_auth_allowed_phonenumbers",
            },
        ),
        migrations.CreateModel(
            name="PhonenumberCheck",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phonenumber",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                ("verified", models.BooleanField(db_index=True, default=False)),
                ("timestamp_requested", models.DateTimeField(auto_now_add=True)),
                ("timestamp_verified", models.DateTimeField(null=True)),
                ("token", models.CharField(max_length=4, null=True)),
            ],
            options={
                "db_table": "mmd_auth_phonenumber_check",
            },
        ),
        migrations.CreateModel(
            name="PhonenumberVerificationLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phonenumber",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("I", "Signin"), ("U", "Signup")], max_length=1
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "success",
                    models.BooleanField(help_text="null if request", null=True),
                ),
            ],
            options={
                "db_table": "mmd_auth_phonenumber_verification_log",
            },
        ),
    ]
