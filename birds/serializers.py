from .models import Birds
from rest_framework import serializers

class BirdSerializer(serializers.ModelSerializer):
  class Meta:
    model = Birds
    fields = ['id', 'subject', 'details']