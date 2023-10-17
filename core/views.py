from .models import Participante, Sala, Presenca
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParticipanteSerializer, SalaSerializer
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime  # Import the datetime module

@api_view(['POST'])
def assign_attendance(request):
    participant_codes = request.data.get('participant_codes', [])  # Get the list of participant codes from the request data

    # Get the current date and time
    current_datetime = datetime.now()

    assigned_participant_codes = set()  # To keep track of participant codes already assigned

    for code in participant_codes:
        try:
            # Assuming 'codigo' is the unique identifier, use filter() instead of get()
            participants = Participante.objects.filter(codigo=code)

            if participants.exists():
                for participant in participants:
                    # Check if the participant code has already been assigned attendance
                    if code not in assigned_participant_codes:
                        # Create a new Presenca instance and populate the data field
                        presenca = Presenca(
                            sala=participant.sala,
                            participante=participant,
                            data=current_datetime  # Assign the current date and time
                        )
                        presenca.save()
                        assigned_participant_codes.add(code)  # Mark this participant code as assigned
            else:
                # Handle participant not found
                pass
        except Participante.DoesNotExist:
            # Handle other exceptions
            pass

    return Response("Attendance assigned successfully", status=status.HTTP_200_OK)


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

