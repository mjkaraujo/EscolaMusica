from django.contrib import admin
from .models import Mensalidade

class MensalidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'vencimento', 'aluno',  'status', 'pagamento', 'valor', 'desc', 'acres', 'total', 'data_criacao', 'ocultar')
    list_display_links = ('id', 'aluno')
    list_per_page = 10
    search_fields = ('id', 'vencimento', 'aluno', 'status')
    list_editable = ('vencimento', 'pagamento', 'status','ocultar', 'desc',  'acres')
    
admin.site.register(Mensalidade, MensalidadeAdmin)

