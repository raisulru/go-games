from django.urls import path
from .views import GameViewSet

urlpatterns = [
    path('games/', GameViewSet.as_view({'get': 'list'}), name='game-list')
]
