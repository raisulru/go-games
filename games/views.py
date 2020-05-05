from rest_framework import serializers, viewsets
from .serializers import GameSerializer
from .models import Game


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
