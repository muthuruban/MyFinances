# Generated by Django 4.2.5 on 2023-09-30 13:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usersettings",
            options={
                "verbose_name": "User Settings",
                "verbose_name_plural": "User Settings",
            },
        ),
    ]
