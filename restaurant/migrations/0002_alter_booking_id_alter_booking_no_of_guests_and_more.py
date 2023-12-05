# Generated by Django 5.0 on 2023-12-05 21:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="ID",
            field=models.IntegerField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="booking",
            name="no_of_guests",
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name="menu",
            name="ID",
            field=models.IntegerField(max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="menu",
            name="inventory",
            field=models.IntegerField(max_length=5),
        ),
    ]
