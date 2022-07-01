from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from .models import Puppy

# Create your views here.
class PuppySerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.URLField()

class PuppyListView(APIView):
    def get(self, request):
        puppies = Puppy.objects.all()
        serialized = PuppySerializer(puppies, many=True)
        data = serialized.data
        return Response(data)