from .models import Dogs
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class DogSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Dogs
    fields = ['id', 'subject', 'details']