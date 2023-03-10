from django.db import models

# Create your models here.
class transformador(models.Model):
    nombre = models.CharField(max_length=15, default='')
    CH4ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    C2H4ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    C2H2ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    H2ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    C2H6ppm = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    t1fallas = models.CharField(max_length=2, default='')
    t4fallas = models.CharField(max_length=2, default='')
    t5fallas = models.CharField(max_length=2, default='')
    