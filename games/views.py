from rest_framework import serializers, viewsets
from django_filters import rest_framework as filters

from .serializers import GameSerializer
from .models import Game


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category',)
