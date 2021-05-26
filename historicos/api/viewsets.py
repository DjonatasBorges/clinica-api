from rest_framework import viewsets
from historicos.models import Historicos
from historicos.api.serialezers import HistoricosSerialezer


class HistoricosViewSet(viewsets.ModelViewSet):
    queryset = Historicos.objects.all().order_by('data')
    serializer_class = HistoricosSerialezer
