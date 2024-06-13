from .models import Dogs
from rest_framework import serializers

class DogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dogs
    fields = ['id', 'subject', 'details']