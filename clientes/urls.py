
from django.contrib import admin
from django.urls import path
from clientes import views

urlpatterns = [

    path('buscar_nomes/', views.buscar_nomes, name='buscar_nomes'),
    path('home/', views.home, name='home'),
    path('lista/', views.lista, name='lista'),
    path('excluir_cliente/<int:id>/', views.excluir_cliente, name='excluir_cliente'),

]
