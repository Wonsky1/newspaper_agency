# Generated by Django 4.2.7 on 2023-11-22 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newspaper", "0002_alter_redactor_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(default=0),
        ),
    ]
