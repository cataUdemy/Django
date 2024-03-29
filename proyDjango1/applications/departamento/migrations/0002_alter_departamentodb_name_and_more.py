# Generated by Django 4.2 on 2023-04-25 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("departamento", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="departamentodb",
            name="name",
            field=models.CharField(blank=True, max_length=50, verbose_name="Nombre"),
        ),
        migrations.AlterField(
            model_name="departamentodb",
            name="short_name",
            field=models.CharField(
                max_length=20, unique=True, verbose_name="Nombre Corto"
            ),
        ),
    ]
