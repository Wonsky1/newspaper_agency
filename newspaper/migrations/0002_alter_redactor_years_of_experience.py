# Generated by Django 4.2.7 on 2023-11-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newspaper", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
