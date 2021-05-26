from rest_framework import viewsets
from agendamentos.models import Agendamentos
from agendamentos.api.serialezers import AgendamentosSerializer


class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('data_hora')
    serializer_class = AgendamentosSerializer
