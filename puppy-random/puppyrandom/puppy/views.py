from django.shortcuts import render

import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from .models import Puppy

# Create your views here.
class PuppySerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.URLField()

    def create(self, validated_data):
        return Puppy.objects.create(**validated_data)

class PuppyListView(APIView):
    def get(self, request):
        if request.method == 'GET':
            puppies = Puppy.objects.all()
            serialized = PuppySerializer(puppies, many=True)
            data = serialized.data
            return Response(data)

class AddPuppy(APIView):
    def post(self, request):
        if request.method == 'POST':
            serialized = PuppySerializer(data=request.data)
            if serialized.is_valid(raise_exception=True):
                serialized.save()
                return Response(serialized.data)

class RandomPuppy():
    pass
