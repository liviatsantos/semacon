from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import AccessToken

from .forms import ProjetoForm
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

@api_view(['POST', 'FILES'])
def criar_projeto(request):
    form = ProjetoForm(request.POST, request.FILES)

    if form.is_valid():
        projeto= form.save(commit=False)
        projeto.save()

        return JsonResponse({'success': True})
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors': form.errors.as_json()}, status=400)