# Generated by Django 2.2.19 on 2021-03-29 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0002_auto_20210324_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoavoto',
            name='opcao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.OpcaoVoto', verbose_name='Opção'),
        ),
    ]