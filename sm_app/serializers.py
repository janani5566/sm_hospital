from rest_framework import serializers
from .models import IPModel

class IpSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPModel
        fields = '__all__'