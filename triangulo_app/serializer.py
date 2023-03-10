from .models import transformador
from rest_framework import serializers

class gasserializer(serializers.ModelSerializer):
    class Meta:
        model = transformador
        fields = '__all__'