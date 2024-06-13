from .models import Cats
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class CatSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Cats
    fields = ['id', 'subject', 'details']