from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista, name='lista'),
    path('detalle/<int:pk>/', views.detalle, name='detalle'),
    path('comprar/<int:pk>/', views.comprar, name='comprar'),
    path('lista_comprado/', views.lista_comprado, name='lista_comprado'),
    path('validar/', views.validarusuario, name='validarUsuario'),
]
