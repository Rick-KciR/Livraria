# Generated by Django 4.1.4 on 2022-12-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("primeiro_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
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
                (
                    "nome",
                    models.CharField(max_length=200, verbose_name="Nome Completo"),
                ),
                ("cpf", models.CharField(max_length=11, verbose_name="Cpf")),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                ("celular", models.CharField(max_length=14, verbose_name="Celular")),
            ],
        ),
    ]