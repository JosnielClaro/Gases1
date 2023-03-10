from rest_framework import viewsets
from .models import transformador
from .serializer import gasserializer

class transformadorviewset(viewsets.ModelViewSet):
    queryset = transformador.objects.all()
    serializer_class = gasserializer