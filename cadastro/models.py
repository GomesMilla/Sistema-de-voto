from django.db import models


class Pessoa(models.Model):

    nome = models.CharField(
        verbose_name = "Nome completo:",
        max_length = 194,
    )

    cpf = models.CharField(
        verbose_name = "Número de CPF:",
        max_length = 11,
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de nascimento:",
        auto_now = False,
        auto_now_add = False,
    )
    email = models.EmailField(
        verbose_name = "Email:",
        max_length = 194,
        unique=True,
    )

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural="Pessoas"
        db_table="Pessoa"

    def __str__(self):
        return self.cpf

class Votacao(models.Model):

    nome = models.CharField(
        verbose_name =  "Nome:",    
        max_length = 194,
    )

    descricao = models.TextField(
        verbose_name = "Insira uma descrição sobre o sistema:",
        max_length = 800,
    )
    anonimo = models.BooleanField(
        verbose_name = "Características da eleição",
        default =False,
    )
    voto_unico = models.BooleanField(
        verbose_name = "Voto unico",
        default = False,
    )
    data_inicio = models.DateField(
        verbose_name = "Data de inicio:",
        auto_now = False,
        auto_now_add = False,
    )
    data_termino = models.DateField(
        verbose_name ="Data termino",
        auto_now = False,
        auto_now_add = False,
    )

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural="Votações"
        db_table="Votacao"

    def __str__(self):
        return self.nome

class OpcaoVoto(models.Model):

    nome = models.CharField(
        verbose_name= "Nome:",
        max_length = 194,
    )

    votacao= models.ForeignKey(
       Votacao,
       on_delete=models.CASCADE)

    codigo = models.CharField(
        verbose_name="Código eleição:",
        max_length =10,

    )
    num_votos = models.CharField(
        verbose_name="Quantidade de votos:",
        max_length = 1000,

    )
    class Meta:
        verbose_name = "Opção Voto"
        verbose_name_plural="Opções de Voto"
        db_table="OpcaoVoto"

    def __str__(self):
        return self.nome


# OpçaõVoto
# —Nome
# —Votação (FK)
# —Codigo
# —N° Votos
# # Create your models here.

# Pessoa
# —Nome
# —CPF
# —DataNascimento
# —Email


# Votação
# —Nome
# —Descrição
# —Anônimo
# —VotoUnico
# —DataInicio
# —DataTermino

