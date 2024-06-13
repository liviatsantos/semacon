from django.urls import path

from . import api

urlpatterns = [
    path('', api.projeto_lista, name='api_projeto_lista'),
]