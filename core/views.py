from .models import Participante, Sala
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParticipanteSerializer, SalaSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

    @api_view(['POST'])
    def create_participantes(request):
        data = request.data.get('participantes', [])  # Get the list of participants from the request data
        serialized_participantes = ParticipanteSerializer(data=data, many=True)
        
        if serialized_participantes.is_valid():
            serialized_participantes.save()
            return Response(serialized_participantes.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_participantes.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

