from distutils.command.upload import upload
from django.utils import timezone
from django.db import models


class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(max_length=8)
    sexo = models.CharField(max_length=10)
    telefone = models.CharField(max_length=11)
    endereço = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    email = models.EmailField(blank=True)
    escolaridade = models.CharField(max_length=255) 
    descricao = models.TextField(blank=True)
    data_inicio = models.DateField(max_length=8)
    curso = models.CharField(max_length=255)
    modulo = models.CharField(max_length=8)   
    responsavel = models.CharField(max_length=255, blank=True)
    cpf_responsavel = models.CharField(max_length=11, blank=True)
    tel = models.CharField(max_length=11, blank=True)
    foto = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    data_criacao = models.DateTimeField(default=timezone.now)
    ocultar = models.BooleanField(default=False)
    

    def __str__(self):
            return "%s %s %s %s %s %s" % (self.id, self.nome, self.sobrenome, self.cpf, self.curso, self.modulo )
