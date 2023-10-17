from rest_framework import serializers
from .models import Sala, Participante, Presenca

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['id', 'nome', 'horario_inicio', 'horario_fim', 'local', 'ativo', 'usuario']

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'

class PresencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenca
        fields = '__all__'  # This includes all fields from the Presenca model