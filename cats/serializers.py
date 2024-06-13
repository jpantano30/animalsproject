from .models import Cats
from rest_framework import serializers

class CatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cats
    fields = ['id', 'subject', 'details']