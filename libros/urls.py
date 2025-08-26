from django.urls import path
from .views import LibroListView, LibroCreateView, LibroUpdateView, LibroDeleteView

urlpatterns = [
    path('', LibroListView.as_view(), name='lista'),
    path('nuevo/', LibroCreateView.as_view(), name='nuevo'),
    path('editar/<int:pk>/', LibroUpdateView.as_view(), name='editar'),
    path('eliminar/<int:pk>/', LibroDeleteView.as_view(), name='eliminar'),
]

