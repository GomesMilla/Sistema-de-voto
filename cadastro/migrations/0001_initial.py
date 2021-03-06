# Generated by Django 2.2.19 on 2021-03-24 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome completo:')),
                ('cpf', models.CharField(max_length=11, verbose_name='Número de CPF:')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento:')),
                ('email', models.EmailField(max_length=194, unique=True, verbose_name='Email:')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'db_table': 'Pessoa',
            },
        ),
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome:')),
                ('descricao', models.TextField(max_length=800, verbose_name='Insira uma descrição sobre o sistema:')),
                ('anonimo', models.BooleanField(verbose_name='Características da eleição')),
                ('voto_unico', models.BooleanField(unique=True, verbose_name='Voto unico')),
                ('data_inicio', models.DateField(verbose_name='Data de inicio:')),
                ('data_termino', models.DateField(verbose_name='Data termino')),
            ],
            options={
                'verbose_name': 'Votacao',
                'verbose_name_plural': 'Votacoes',
                'db_table': 'Votacao',
            },
        ),
        migrations.CreateModel(
            name='OpcaoVoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome:')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código eleição:')),
                ('num_votos', models.CharField(max_length=1000, verbose_name='Quantidade de votos:')),
                ('votacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Votacao')),
            ],
            options={
                'verbose_name': 'OpcaoVoto',
                'verbose_name_plural': 'Opcoesvoto',
                'db_table': 'OpcaoVoto',
            },
        ),
    ]
