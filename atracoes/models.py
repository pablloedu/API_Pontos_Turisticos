from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField(max_length=150)
    idade_minima = models.IntegerField()
    aprovado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='imagens/atracoes', null=True, blank=True)

    def __str__(self):
        return self.nome