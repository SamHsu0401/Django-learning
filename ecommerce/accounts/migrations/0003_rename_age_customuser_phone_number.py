# Generated by Django 4.2.3 on 2023-07-19 20:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_remove_customuser_phone_number_customuser_age"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser",
            old_name="age",
            new_name="phone_number",
        ),
    ]
