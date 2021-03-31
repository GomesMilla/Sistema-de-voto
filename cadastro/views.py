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
import datetime
# from django.contrib.auth.decorators import login_required



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

            
            return redirect("cadastrar_pessoa")

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
    
    
    context = {
        "listPessoa": allpessoas,
    }

    
    return render(request, "listar_pessoas.html", context)

def listar_votacao (request):
    allvotacoes = Votacao.objects.all()

    
    context = {
        "listVotacao": allvotacoes,
    }
    return render(request, "listavotacao.html", context)

def votacoes_disponiveis (request):
    today = datetime.date.today()

    allvotacoes = Votacao.objects.filter(data_inicio__lte=today, data_termino__gte=today)
    
    context = {
        "listVotacao": allvotacoes,
    }
    return render(request, "votacoesdisponiveis.html", context)
# @login_required
def home(request):

    context = {
        "home" : home,
    }

    return render(request, "home.html", context)
   



