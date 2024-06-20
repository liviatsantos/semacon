from django.forms import ModelForm

from .models import Projeto

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = {
            'descricao',
            'data_inicio',
            'niveis',
            'area_total',
            'imagem',

        }