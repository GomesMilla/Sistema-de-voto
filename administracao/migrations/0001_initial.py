# Generated by Django 2.2.19 on 2021-03-24 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaVoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.OpcaoVoto')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Pessoa')),
                ('votacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Votacao')),
            ],
        ),
    ]
