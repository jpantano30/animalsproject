from django.shortcuts import render
from .models import Birds
from rest_framework import viewsets, permissions
from .serializers import BirdSerializer

class BirdViewSet(viewsets.ModelViewSet):
  queryset = Birds.objects.all()
  serializer_class = BirdSerializer
  permission_classes = [permissions.AllowAny]
