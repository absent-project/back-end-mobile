from .models import Sala
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from .serializers import SalaSerializer, ParticipanteSerializer
# Create your views here.
class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = ParticipanteSerializer

    @api_view(['POST'])
    def post(request):
        ser = ParticipanteSerializer(request.data, many = True)
        print(ser.data)