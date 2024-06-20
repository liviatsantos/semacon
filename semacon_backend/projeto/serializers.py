from rest_framework import serializers 
from .models import Projeto

class ProjetoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = (
            'id',
            'descricao',
            'data_inicio',
            'niveis',
            'area_total',
            'imagem_url',
        )