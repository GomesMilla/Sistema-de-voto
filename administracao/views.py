from django.shortcuts import render, redirect
from administracao.models import *
from django.contrib import messages
from cadastro.models import *

def votar(request, id_votacao, id_pessoa):


    context = {
        "id_pessoa": id_pessoa,
        "id_votacao" : id_votacao,
    }


    return render (request,"votar.html", context)

    



def apuracao(request, id_votacao):

    controleOpcaodeVoto = Opcaovoto.objects.get(pk=id_votacao)
    controlePessoavoto= PessoaVoto.objects.filter(OpcaoVoto=controleOpcaodeVoto)

    context = {
        "allVotacions" : controlePessoaVoto,
        
    }

    return render(request,"home.html",context)




def validacao(request, id_votacao):
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


# Create your views here.
