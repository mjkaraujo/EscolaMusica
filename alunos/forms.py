from django.forms import ModelForm
from django.db import models
from .models import Aluno
from django import forms

SEXO_CHOICES = [('Feminino','Feminino'), ('Masculino','Masculino')]
ESCOLARIDADE_CHOICES = [
        ('Ensino Fundamental', 'Ensino Fundamental'),
        ('Ensino Médio', 'Ensino Médio'),
        ('Ensino Técnico', 'Ensino Técnico'),
        ('Superior Completo', 'Superior Completo')
]
MODULO_CHOICES = [
        ('MB-1', 'MB-1'),
        ('MB-2', 'MB-2'),
        ('MOD-1', 'MOD-1'),
        ('MOD-2', 'MOD-2'),
        ('MOD-3', 'MOD-3'),
]
CURSOS_CHOICES = [
        ('Guitarra', 'Guitarra'),
        ('Violão', 'Violão'),
        ('Teclado', 'Teclado'),
        ('Baixo', 'Baixo'),
        ('Bateria', 'Bateria'),
        ('Canto', 'Canto'),
        ('Percepção Musical', 'Percepção Musical'),
        ('Introdução a Teoria Musical', 'Introdução a Teoria Musical'),
        ('Harmonia Funcional', 'Harmonia Funcional'),
]

class FormAlunos (forms.ModelForm):
        class Meta:
                model = Aluno
                fiels = '__all__'
                widgets = {
                        'sexo': forms.RadioSelect(choices=SEXO_CHOICES),
                        'escolaridade': forms.Select(choices=ESCOLARIDADE_CHOICES),
                        'curso': forms.Select(choices=CURSOS_CHOICES),
                        'modulo': forms.Select(choices=MODULO_CHOICES),
                        'data_nascimento': forms.SelectDateWidget(years=range(1950,2050)),
                        'data_inicio': forms.SelectDateWidget(),
                        } 
                
                exclude = ('ocultar', 'data_criacao',)