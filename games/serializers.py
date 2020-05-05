from rest_framework import serializers
from .models import Game, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class GameSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Game
        fields = [
            'id',
            'name',
            'image',
            'category'
        ]