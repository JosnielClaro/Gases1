from rest_framework import viewsets
from .models import transformador, Nombre
from .serializer import gasserializer, nombreserializer

class transformadorviewset(viewsets.ModelViewSet):
    queryset = transformador.objects.all()
    serializer_class = gasserializer
    
class nombreviewset(viewsets.ModelViewSet):
    queryset = Nombre.objects.all()
    serializer_class = nombreserializer