from django.shortcuts import render
from .models import Dogs
from rest_framework import viewsets, permissions
from .serializers import DogSerializer

class DogViewSet(viewsets.ModelViewSet):
  queryset = Dogs.objects.all()
  serializer_class = DogSerializer
  permission_classes = [permissions.AllowAny]
