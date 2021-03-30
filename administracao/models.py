from django.db import models
from cadastro.models import *

class PessoaVoto(models.Model):

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name= "Pessoa:")
    votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE)
    opcao = models.ForeignKey(OpcaoVoto, on_delete=models.CASCADE, verbose_name = "Opção")
    quantidade_votos = models.PositiveSmallIntegerField(verbose_name = "Quantidade de Votos:",default= 0,)

    class Meta:
        verbose_name = "Votação:"
        verbose_name_plural = "Votações:"
        db_table = "PessoaVoto"

    def __str__(self):
        return self.votacao
