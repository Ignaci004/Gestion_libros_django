from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import re

# --- VALIDACIÓN DE FECHA ---
def validar_fecha_no_futura(fecha):
    if fecha > timezone.now().date():
        raise ValidationError("La fecha de publicación no puede ser futura.")

# --- VALIDACIÓN SOLO LETRAS (para título) ---
def validar_solo_letras(valor):
    if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$', valor):
        raise ValidationError("El título solo puede contener letras y espacios.")

# --- VALIDACIÓN PARA NOMBRES DE AUTOR ---
def validar_nombre_autor(valor):
    if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúñÑ .\'-]+$', valor):
        raise ValidationError("El nombre del autor solo puede contener letras, espacios, puntos, guiones o apóstrofes.")

class Libro(models.Model):
    titulo = models.CharField(
        max_length=200,
        validators=[validar_solo_letras]
    )
    autor = models.CharField(
        max_length=200,
        validators=[validar_nombre_autor]
    )
    fecha_publicacion = models.DateField(validators=[validar_fecha_no_futura])
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
