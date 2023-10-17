from rest_framework import serializers
from .models import Sala, Participante

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['id', 'nome', 'horario_inicio', 'horario_fim', 'local', 'ativo', 'usuario']

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['id', 'nome', 'codigo', 'sala']

    