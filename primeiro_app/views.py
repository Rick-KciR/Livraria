from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Livro
from datetime import datetime
from .form import LivroForm


def home(request):
    dados = {"agora": datetime.now()}
    return render(request, "primeiro_app/home.html", dados)


def listagem(request):
    dados = {"Livros": Livro.objects.all()}
    return render(request, "primeiro_app/listagem.html", dados)


def criar(request):
    dados = {}
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")
    dados["form"] = form
    return render(request, "primeiro_app/form.html", dados)

