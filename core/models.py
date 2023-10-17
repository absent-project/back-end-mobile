from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Sala(models.Model):
    nome = models.CharField( max_length=5000)
    horario_inicio = models.TimeField( auto_now=False, auto_now_add=False)
    horario_fim = models.TimeField( auto_now=False, auto_now_add=False)
    local = models.CharField( max_length=5000)
    ativo = models.BooleanField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Participante(models.Model):
    nome = models.CharField( max_length=2000)
    codigo = models.CharField(max_length=5000)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

class Presenca(models.Model):
    data = models.DateTimeField( auto_now=False, auto_now_add=False)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)