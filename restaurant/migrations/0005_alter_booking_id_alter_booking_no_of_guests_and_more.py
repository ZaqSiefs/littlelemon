# Generated by Django 5.0 on 2023-12-08 22:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0004_alter_booking_id_alter_booking_no_of_guests_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="ID",
            field=models.PositiveSmallIntegerField(
                primary_key=True,
                serialize=False,
                validators=[django.core.validators.MaxValueValidator(24)],
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="no_of_guests",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MaxValueValidator(15)]
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="ID",
            field=models.PositiveSmallIntegerField(
                primary_key=True,
                serialize=False,
                validators=[django.core.validators.MaxValueValidator(100)],
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="inventory",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MaxValueValidator(200)]
            ),
        ),
    ]
