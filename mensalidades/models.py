from distutils.command.upload import upload
from django.utils import timezone
from alunos.models import Aluno
from django.db import models


class Mensalidade(models.Model):
    id = models.AutoField(primary_key=True)
    vencimento = models.DateField(max_length=8)
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, verbose_name='Aluno')
    status = models.CharField(max_length=8)
    pagamento = models.DateField(max_length=8, blank=True, null=True, default=None)
    valor = models.FloatField()
    desc = models.FloatField()   
    acres = models.FloatField()
    total = models.FloatField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    ocultar = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
         self.total = self.valor - self.desc + self.acres
         super().save(*args, **kwargs)

    def __str__(self):
            return self.id
    
    class Meta:
        verbose_name = 'Mensalidade'
        verbose_name_plural = 'Mensalidades'
