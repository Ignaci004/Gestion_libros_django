from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Libro

class LibroListView(ListView):
    model = Libro
    template_name = "libros/lista.html"

class LibroCreateView(CreateView):
    model = Libro
    fields = ['titulo', 'autor', 'genero', 'fecha_publicacion']
    template_name = "libros/form.html"
    success_url = reverse_lazy('lista')

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['titulo', 'autor', 'genero', 'fecha_publicacion']
    template_name = "libros/form.html"
    success_url = reverse_lazy('lista')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libros/eliminar.html"
    success_url = reverse_lazy('lista')
