from rest_framework import serializers

from .models import RandomUUID

class RandomUUIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomUUID
        fields = ['cowrytest_name', 'timestamp', 'time']
