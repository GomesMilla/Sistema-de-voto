from django.db import models
from cadastro.models import *

class PessoaVoto(models.Model):

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name= "Pessoa:")
    votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE)
    opcao = models.ForeignKey(OpcaoVoto, on_delete=models.CASCADE)
