from django.contrib import admin
from .models import Professores

class ProfessoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'cpf', 'data_nascimento','sexo','telefone','endereço','bairro','cidade','cep', 'email', 'escolaridade','descricao', 'instrumento', 'foto', 'data_criacao', 'ocultar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone', 'email')
    list_editable = ('telefone', 'ocultar', 'instrumento', 'endereço', 'bairro', 'cidade', 'cep', 'email', 'escolaridade', 'descricao')
    
admin.site.register(Professores, ProfessoresAdmin)
