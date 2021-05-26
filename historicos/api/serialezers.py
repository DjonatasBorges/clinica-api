from rest_framework import serializers
from historicos.models import Historicos


class HistoricosSerialezer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = '__all__'
