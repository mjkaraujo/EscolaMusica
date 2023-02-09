from ast import arg
from http.client import ImproperConnectionState
import os
from pickletools import optimize
from turtle import heading
from django.db import models
from albuns.models import Albuns
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

class Fotos(models.Model):
    titulo_fotos = models.CharField(max_length=255, verbose_name='Titulo')
    autor_fotos = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_fotos = models .DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_fotos = models.TextField(verbose_name='Conteudo') 
    excerto_fotos = models .TextField(verbose_name='excerto')
    imagem_fotos = models.ImageField(upload_to='fotos_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem') 
    albuns_fotos = models.ForeignKey(Albuns, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Albuns') 
    publicado_fotos = models.BooleanField(default=False, verbose_name='Publicado') 

    def __str__(self):
        return self.titulo_fotos

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

