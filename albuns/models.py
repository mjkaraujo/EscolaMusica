from django.db import models

class Albuns(models.Model):
    nome_albuns = models.CharField(max_length=50, verbose_name='Albuns')

    def __str__(self):
        return self.nome_albuns

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'

