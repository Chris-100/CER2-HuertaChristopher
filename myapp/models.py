from django.db import models
import datetime

# Create your models here.
class Residencia(models.Model):
    residencia = models.CharField(max_length=6)
    Propietario = models.CharField(max_length=30)

    def __str__(self):
        return self.residencia

class correspondencia(models.Model):
    fecha = models.DateField(default=datetime.date.today)
    recivio = models.CharField(max_length=30)
    residencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return self.residencia.residencia
