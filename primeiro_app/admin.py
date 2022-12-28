from django.contrib import admin

from primeiro_app.models import Autor, Livro, Categoria


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...

