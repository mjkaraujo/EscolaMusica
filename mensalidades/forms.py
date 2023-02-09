from django.forms import ModelForm
from django.db import models
from .models import Mensalidade
from django import forms


STATUS_CHOICES = [
        ('aberta', 'aberta'),
        ('fechada', 'fechada'),
        ('vencida', 'vencida'),
]

class FormMensalidade (forms.ModelForm):
        class Meta:
                model = Mensalidade
                fiels = '__all__'
                widgets = {
                        'status': forms.Select(choices=STATUS_CHOICES),
                        'vencimento': forms.SelectDateWidget(),
                        'pagamento': forms.SelectDateWidget(),
                        'total': forms.TextInput(attrs={'readonly': 'readonly'}),
                        } 
                labels = {
                        'id': 'ID',
                        'vencimento': 'Vencimento',
                        'aluno': 'Aluno',
                        'status': 'Status',
                        'pagamento': 'Pagamento',
                        'valor': 'Valor',
                        'desc': 'Desconto',
                        'acres': 'Acréscimo',
                        'total': 'Total',
                }
                
                exclude = ('ocultar', 'data_criacao',)