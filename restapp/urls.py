from django.urls import path
from .views import Categoria_list, Categoria_detalle

urlpatterns = [
    path('Categorias/',Categoria_list, name ='Categoria_list'),
    path('Categorias/<int:pk>',Categoria_detalle, name = 'Categoria_detalle')
]