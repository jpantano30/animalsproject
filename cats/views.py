from django.shortcuts import render
from .models import Cats
from rest_framework import viewsets, permissions
from .serializers import CatSerializer

class CatViewSet(viewsets.ModelViewSet):
  queryset = Cats.objects.all()
  serializer_class = CatSerializer
  permission_classes = [permissions.AllowAny]
