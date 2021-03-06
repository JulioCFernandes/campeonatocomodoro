# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171003_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combinacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('faixa', models.IntegerField(choices=[(1, 'Branca'), (2, 'Cinza / Branca'), (3, 'Cinza'), (4, 'Cinza / Preta'), (5, 'Amarela Branca'), (6, 'Amarela'), (7, 'Amarela / Preta'), (8, 'Laranja / Branca'), (9, 'Laranja'), (10, 'Laranja / Preta'), (11, 'Verde / Branca'), (12, 'Verde'), (13, 'Verde / Preta'), (14, 'Azul'), (15, 'Roxa'), (16, 'Marrom'), (17, 'Preta'), (18, 'Vermelha / Preta'), (19, 'Vermelha / Branca'), (20, 'Vermelha')])),
                ('idade', models.IntegerField(choices=[(1, 'Pré-Mirin'), (2, 'Mirin'), (3, 'Infantil'), (4, 'Infanto Juvenil'), (7, 'Juvenil'), (5, 'Adulto'), (6, 'Master')])),
                ('peso', models.IntegerField(choices=[(1, 'Galo'), (2, 'Pluma'), (3, 'Pena'), (4, 'Leve'), (5, 'Médio'), (6, 'Meio Pesado'), (7, 'Pesado'), (8, 'Super Pesado'), (9, 'Pesadíssimo')])),
            ],
            options={
                'verbose_name': 'combinação',
                'verbose_name_plural': 'combinações',
            },
        ),
        migrations.CreateModel(
            name='Confronto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confronto', models.IntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('faixa', models.IntegerField(choices=[(1, 'Branca'), (2, 'Cinza / Branca'), (3, 'Cinza'), (4, 'Cinza / Preta'), (5, 'Amarela Branca'), (6, 'Amarela'), (7, 'Amarela / Preta'), (8, 'Laranja / Branca'), (9, 'Laranja'), (10, 'Laranja / Preta'), (11, 'Verde / Branca'), (12, 'Verde'), (13, 'Verde / Preta'), (14, 'Azul'), (15, 'Roxa'), (16, 'Marrom'), (17, 'Preta'), (18, 'Vermelha / Preta'), (19, 'Vermelha / Branca'), (20, 'Vermelha')])),
                ('categoria_peso', models.IntegerField(choices=[(1, 'Galo'), (2, 'Pluma'), (3, 'Pena'), (4, 'Leve'), (5, 'Médio'), (6, 'Meio Pesado'), (7, 'Pesado'), (8, 'Super Pesado'), (9, 'Pesadíssimo')], default=1, verbose_name='Peso')),
                ('categoria_idade', models.IntegerField(choices=[(1, 'Pré-Mirin'), (2, 'Mirin'), (3, 'Infantil'), (4, 'Infanto Juvenil'), (7, 'Juvenil'), (5, 'Adulto'), (6, 'Master')], default=5, verbose_name='Idade')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='inscricao',
            options={'verbose_name': 'inscrição', 'verbose_name_plural': 'incrições'},
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='categoria_idade',
            field=models.IntegerField(choices=[(1, 'Pré-Mirin'), (2, 'Mirin'), (3, 'Infantil'), (4, 'Infanto Juvenil'), (7, 'Juvenil'), (5, 'Adulto'), (6, 'Master')], default=5, verbose_name='Idade'),
        ),
        migrations.AddField(
            model_name='confronto',
            name='inscricao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Inscricao', verbose_name='inscrição'),
        ),
        migrations.AddField(
            model_name='combinacao',
            name='inscricao',
            field=models.ManyToManyField(to='core.Inscricao'),
        ),
    ]
