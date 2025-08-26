from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()  # <-- Agregado
    genero = models.CharField(max_length=100)  # <-- Agregado

    def __str__(self):
        return self.titulo
