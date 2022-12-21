from django.contrib import admin

from primeiro_app.models import Autor, Livro, Categoria, Cliente, Endereco


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    ...


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    ...
