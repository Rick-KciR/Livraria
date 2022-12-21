# Generated by Django 4.1.4 on 2022-12-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("primeiro_app", "0003_endereco"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name_plural": "Autores"},
        ),
        migrations.AlterModelOptions(
            name="categoria",
            options={"verbose_name_plural": "Categorias"},
        ),
        migrations.AlterModelOptions(
            name="cliente",
            options={"verbose_name_plural": "Clientes"},
        ),
        migrations.AlterModelOptions(
            name="endereco",
            options={"verbose_name_plural": "Endereços"},
        ),
        migrations.AlterModelOptions(
            name="livro",
            options={"verbose_name_plural": "Livros"},
        ),
        migrations.AlterField(
            model_name="livro",
            name="valor",
            field=models.DecimalField(
                decimal_places=2, default=99.99, max_digits=7, verbose_name="Valor"
            ),
        ),
    ]