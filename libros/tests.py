from django.test import TestCase
from datetime import date
from libros.models import Libro

class LibroModelTest(TestCase):
    def test_guardar_libro(self):
        libro = Libro.objects.create(
            titulo="El Quijote",
            autor="Cervantes",
            genero="Novela",
            fecha_publicacion=date(1605, 1, 16)
        )
        self.assertEqual(libro.titulo, "El Quijote")
