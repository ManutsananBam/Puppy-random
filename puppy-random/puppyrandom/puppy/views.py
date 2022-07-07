from rest_framework import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Puppy

import random

# Create your views here.
class PuppySerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.URLField()

    def create(self, validated_data):
        return Puppy.objects.create(**validated_data)


class PuppyList(generics.ListCreateAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer

class PuppyRandom(APIView):
    def get(self, request):
        puppies = Puppy.objects.all()
        ids = puppies.values_list('id', flat=True)
        random_id = random.choice(ids)
        return Response(random_id)
        
