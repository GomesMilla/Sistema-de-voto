"""estrutura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cadastro.views import (
    cadastrar_pessoa, registrar_opcao_de_voto, registrar_votacao, listar_pessoas, listar_votacao, votacoes_disponiveis, home)
from  administracao.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path("cadastrar-pessoa/", cadastrar_pessoa, name= "cadastrar_pessoa",),
    
    path("registrar-opcao-de-voto/", registrar_opcao_de_voto, name= "registrar_opcao_de_voto", ),

    path("registrar-votacao/", registrar_votacao, name= "registrar_votacao",),
    
    path("listar-pessoas/", listar_pessoas, name="listar_pessoas",),
    
    path("listar-votacao/", listar_votacao, name="listar_votacao",),

    path("votacoes_disponiveis/", votacoes_disponiveis, name="votacoes_disponiveis"),

    path("validacao/<int:id_votacao>/", validacao, name="validacao",),

    path("votar/<int:id_votacao>/<int:id_pessoa>/", votar, name="votar",),

    path("apuracao/", apuracao, name="apuracao",),

    path("", home, name= "home",),
]

