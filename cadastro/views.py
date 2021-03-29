from django.shortcuts import render
from django.shortcuts import(
    render, redirect, get_object_or_404
)
from cadastro.models import *
from cadastro.forms import PessoaForm
from cadastro.forms import VotacaoForm
from cadastro.forms import OpcaoVotoForm
from templates import *
from django.contrib import messages



def cadastrar_pessoa(request):
    
    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            
            form.save()

            return redirect("cadastrar_pessoa")
            
    context={
        "nome_pagina":"Registrar Pessoa",
        "form":form
    }

    return render (request,"index.html", context)

def registrar_votacao(request):
    
    form = VotacaoForm()

    if request.method == "POST":
        form = VotacaoForm(request.POST)

        if form.is_valid():
           
            form.save()

            
            return redirect("cadastar_pessoa")

    context={
        "nome_pagina":"Registrar votação",
        "form":form
        }
    
    return render (request,"votacao.html", context)

def registrar_opcao_de_voto(request):
    
    form = OpcaoVotoForm()

    if request.method == "POST":
        form = OpcaoVotoForm(request.POST)

        if form.is_valid():
            
            form.save()
            
            return redirect("registrar_votacao")
    
    context={
        "nome_pagina":"Registrar opção de voto",
        "form":form
    }

    return render (request,"opcao.html", context)

def listar_pessoas(request):
    allpessoas = Pessoa.objects.all()
    listaPessoas = []

    for aux in allpessoas:
        listaPessoas.append(aux)

    context = {
        "listaPessoas": listaPessoas,
    }

    return render(request, "listar_pessoas.html", context)





