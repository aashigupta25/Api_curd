from rest_framework import serializers
from .models import APIoperation

class APIoperationSerializer(serializers.Serializer):
    create = serializers.CharField(max_length = 100)    
    update = serializers.CharField(max_length = 100)
    retrieve = serializers.CharField(max_length = 100)
    delete = serializers.CharField(max_length = 100)


def create(self, validated_data):
    return APIoperation.objects.create(**validated_data)