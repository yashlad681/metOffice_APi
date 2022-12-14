# Generated by Django 4.1.3 on 2022-11-23 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WeatherData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                ("jan", models.FloatField()),
                ("feb", models.FloatField()),
                ("mar", models.FloatField()),
                ("apr", models.FloatField()),
                ("may", models.FloatField()),
                ("jun", models.FloatField()),
                ("jul", models.FloatField()),
                ("aug", models.FloatField()),
                ("sep", models.FloatField()),
                ("oct", models.FloatField()),
                ("nov", models.FloatField()),
                ("dec", models.FloatField()),
                ("winter", models.FloatField()),
                ("spring", models.FloatField()),
                ("summer", models.FloatField()),
                ("autumn", models.FloatField()),
                ("annual", models.FloatField()),
            ],
        ),
    ]
