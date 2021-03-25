from django import forms
from cadastro.models import *

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = (
           "nome", "cpf", "email",
        )

class VotacaoForm(forms.ModelForm):

    class Meta:
        model = Votacao
        fields = (
            "nome", "descricao", "data_inicio", "data_termino",
        )

class OpcaoVoto(forms.ModelForm):
   
    class Meta:
        model = OpcaoVoto
        fields = (
            "nome", "codigo", 
        )