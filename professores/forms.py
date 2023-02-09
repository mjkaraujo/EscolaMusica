from django.forms import ModelForm
from django.db import models
from .models import Professores
from django import forms


SEXO_CHOICES = [('Feminino','Feminino'), ('Masculino','Masculino')]
ESCOLARIDADE_CHOICES = [
        ('Ensino Fundamental', 'Ensino Fundamental'),
        ('Ensino Médio', 'Ensino Médio'),
        ('Ensino Técnico', 'Ensino Técnico'),
        ('Superior Completo', 'Superior Completo')
]

class FormProfessores (forms.ModelForm):
        class Meta:
                model = Professores
                fiels = '__all__'
                widgets = {
                        'sexo': forms.RadioSelect(choices=SEXO_CHOICES),
                        'escolaridade': forms.Select(choices=ESCOLARIDADE_CHOICES),
                        'data_nascimento': forms.SelectDateWidget(years=range(1950,2050)),
                        'data_inicio': forms.SelectDateWidget(),
                        } 
                
                exclude = ('ocultar', 'data_criacao',)