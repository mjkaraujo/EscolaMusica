from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'cpf', 'data_nascimento','sexo','telefone','endereço','bairro','cidade','cep', 'email', 'escolaridade','descricao', 'curso', 'modulo', 'foto', 'responsavel', 'cpf_responsavel', 'tel', 'data_criacao', 'ocultar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone', 'email')
    list_editable = ('telefone', 'ocultar', 'curso', 'modulo', 'endereço', 'bairro', 'cidade', 'cep', 'email', 'escolaridade', 'descricao')
    
admin.site.register(Aluno, AlunoAdmin)
