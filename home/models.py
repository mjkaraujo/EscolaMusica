from django.db import models

class Contatos(models.Model):
    nome_contato = models.CharField(max_length=150, verbose_name='Nome') 
    email_contato = models.EmailField(verbose_name='Email') 
    telefone_contato = models.CharField(max_length=14,verbose_name='Telefone')  
    mensagem_contato = models.TextField(verbose_name='Mensagem')  
    
    def __str__(self):
            return self.nome_contato
