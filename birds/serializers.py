from .models import Birds
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class BirdSerializer(serializers.HyperlinkModelSerializer):
  class Meta:
    model = Birds
    fields = ['id', 'subject', 'details']