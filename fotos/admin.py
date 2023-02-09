from django.contrib import admin
from .models import Fotos

class FotosAdmin(admin.ModelAdmin):
    list_display = ('id','titulo_fotos', 'autor_fotos', 'data_fotos', 'albuns_fotos', 'publicado_fotos',)
    list_editable = ('publicado_fotos',)
    list_display_links = ('id', 'titulo_fotos',)

admin.site.register(Fotos, FotosAdmin)
