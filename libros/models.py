from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validar_fecha_no_futura(fecha):
    if fecha > timezone.now().date():
        raise ValidationError("La fecha de publicación no puede ser futura.")

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField(validators=[validar_fecha_no_futura])
    genero = models.CharField(max_length=100)
#nose
    def __str__(self):
        return self.titulo


