from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import AccessToken

from .models import Projeto
from .serializers import ProjetoListaSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def projeto_lista(request):
    projetos = Projeto.objects.all()
    serializer = ProjetoListaSerializer(projetos, many=True)

    return JsonResponse({
        'data': serializer.data
    })