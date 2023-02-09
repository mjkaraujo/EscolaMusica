from django.contrib import admin
from .models import Albuns

class AlbunsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_albuns')
    list_display_links = ('id', 'nome_albuns')

admin.site.register(Albuns, AlbunsAdmin)


