from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome') 
    email_comentario = models.EmailField(verbose_name='email') 
    comentario = models.TextField(verbose_name='comentario')  
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')  
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING,blank=True, null=True, verbose_name='Usuario')  
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name='Data')  
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado')  

    def __str__(self):
            return self.nome_comentario
