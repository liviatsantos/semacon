import uuid

from django.conf import settings
from django.db import models

from useraccount.models import User

class Projeto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    niveis = models.IntegerField()
    area_total = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    
