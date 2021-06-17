from django.shortcuts import render
from rest_framework import viewsets

from .serializers import GameSerializer, PlatformSerializer
from .models import Game, Platform

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
