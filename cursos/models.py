from django.db import models

class ContatoCurso(models.Model):
    nome_curso = models.CharField(max_length=150, verbose_name='Nome') 
    email_curso = models.EmailField(verbose_name='Email') 
    telefone_curso = models.CharField(max_length=14,verbose_name='Telefone')  
    mensagem_curso = models.TextField(verbose_name='Mensagem')  
    
    def __str__(self):
            return self.nome__curso
