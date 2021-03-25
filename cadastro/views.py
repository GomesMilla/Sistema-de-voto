from django.shortcuts import render
from django.shortcuts import(
    render, redirect, get_object_or_404
)
from cadastro.models import *
from cadastro.forms import PessoaForm
from templates import *


def cadastrar_pessoa(request):
    
    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save(commit = False)

            
            return redirect("cadastrar_pessoa")

    return render (request,"index.html", {"form":form})

def Votacao_em_si(request):
    
    form = VotacaoForm()

    if request.method == "POST":
        form = VotacaoForm(request.POST)

        if form.is_valid():
            pessoa = form.save(commit = False)

            
            return redirect("opcao_de_voto")
    return render (request,"votacao.html", {"form":form})

def opcao_de_voto(request):
    
    form = OpcaoVotoForm()

    if request.method == "POST":
        form = OpcaoVotoForm(request.POST)

        if form.is_valid():
            pessoa = form.save(commit = False)

            
            return redirect("Votacao_em_si")

    return render (request,"opcao.html", {"form":form})



# Create your views here.
