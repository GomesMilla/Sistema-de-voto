from django import forms
from cadastro.models import *

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = (
           "nome", "cpf", "email", "data_nascimento",
        )

        error_messages = {
            "nome":{
                "required": "O nome é obrigatório para o registro",
            },

            "cpf": {
                "required" : "CPF é obrigatório para o registro de cadastro.",
            },

            "email":{
                "required" : "Email é obrigatório para o cadastro",
                "invalid": "Por favor, informe um formato válido para o email",
            },

            "data_nascimento":{
                "required" : "Data de nascimento é obrigatória e deve ser no formato AAAA/MM/DD.",
                "invalid": "Por favor, informe um formato válido para a data",
            },
        }

class VotacaoForm(forms.ModelForm):

    class Meta:
        model = Votacao
        fields = (
            "nome", "descricao", "data_inicio", "data_termino",
        )
        error_messages = {
            "nome":{
                "required": "O nome é obrigatório para o registro",
            },

            "descricao": {
                "required" : "A descrição é obrigatória!",
            },

            "data_inicio":{
                "required" : "Data do inicio da eleição é obrigatória e deve ser no formato AAAA-MM-DD",
                "invalid": "Por favor, informe um formato válido para a data",
            },

            "data_termino":{
                "required" : "Data do termino é obrigatória e deve ser no formato AAAA-MM-DD.",
                "invalid": "Por favor, informe um formato válido para a data",
            },
        }

class OpcaoVotoForm(forms.ModelForm):
   
    class Meta:
        model = OpcaoVoto
        fields = (
            "nome", "codigo", "votacao", 
        )
        error_messages = {
            "nome":{
                "required": "O nome é obrigatório para o registro",
            },
            "codigo":{
                "required": "Código é obrigatório.",
            },

            "votacao":{
                "required": "Tipo de votação é necessário, porfavor selecione um",
            },
        }