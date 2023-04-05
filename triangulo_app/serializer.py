from .models import transformador, Nombre
from rest_framework import serializers

class gasserializer(serializers.ModelSerializer):
    class Meta:
        model = transformador
        fields = ('__all__')
        
class nombreserializer(serializers.ModelSerializer):
    class Meta:
        model = Nombre
        fields = ('__all__')