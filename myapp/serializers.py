from rest_framework import serializers
from .models import GeneralPost, SardorPost, ZoirPost, JasurPost

class GeneralPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralPost
        fields = '__all__'

class SardorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SardorPost
        fields = '__all__'

class ZoirPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoirPost
        fields = '__all__'

class JasurPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JasurPost
        fields = '__all__'
