from django.db import models

# Create your models here.


class Nombre(models.Model):
    nombre = models.CharField(max_length=30, default='')
    def __str__ (self):
        return self.nombre
    
class transformador(models.Model):
    nombre = models.ForeignKey(Nombre, null=True, blank=True,    on_delete=models.CASCADE)
    CH4ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    C2H4ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    C2H2ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    H2ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    C2H6ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    t1fallas = models.CharField(max_length=2, default='', null=True)
    t4fallas = models.CharField(max_length=2, default='', null=True)
    t5fallas = models.CharField(max_length=2, default='', null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-id']
    