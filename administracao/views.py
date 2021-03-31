from django.shortcuts import render, redirect
from administracao.models import *
from django.contrib import messages
from cadastro.models import *
import datetime
# from django.contrib.auth.decorators import login_required

def votar(request, id_votacao, id_pessoa):

    people = Pessoa.objects.get(pk=id_pessoa)
    voto = Votacao.objects.get(pk=id_votacao)
    listoption = OpcaoVoto.objects.filter(votacao=voto)

    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = OpcaoVoto.objects.get(pk=idOpcaoVoto)
        objOpcaoVoto.num_votos += 1
        objOpcaoVoto.save()
    
        return redirect("home")
    
    context = {

        "listoption" : listoption,
        "people": people, 

    }
    return render (request,"votar.html", context)

    

def apuracao(request, id_votacao):
    
    controlevotacao = Votacao.objects.get(pk=id_votacao)
    controleOpcaodeVoto = OpcaoVoto.objects.filter(votacao=controlevotacao)

    context = {
        "controleOpcaodeVoto" : controleOpcaodeVoto,
        
    }

    return render(request,"apuracao.html", context)




def validacao(request, id_votacao):
    objvotacao = Votacao.objects.get(pk=id_votacao)
   
    if objvotacao.data_inicio > datetime.date.today() or objvotacao.data_termino < datetime.date.today():
        messages.error(request, "Votação não esta disponivel!")
        return redirect("listar_votacao")
    if request.POST:
        
        validacao_de_cpf = request.POST.get('cpf', None)

        try:
            objpessoa = Pessoa.objects.get(cpf=validacao_de_cpf)
            id_pessoa = objpessoa.id
            print(validacao_de_cpf)



            return redirect("votar",id_votacao,id_pessoa) 
            
        except Pessoa.DoesNotExist:
        
            messages.error(request,"Pessoa não cadastrada!")
    
    return render (request, "validacao.html",)

def resultado_apuracao(request):

    context = {
        "home" : home,
    }
    return render(request, "home.html")


# Create your views here.
