from rest_framework import serializers
from rest_framework import generics

from .models import Puppy

# Create your views here.
class PuppySerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.URLField()

    def create(self, validated_data):
        return Puppy.objects.create(**validated_data)

class PuppyList(generics.ListCreateAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer

