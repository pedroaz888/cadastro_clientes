
from django.contrib import admin
from django.urls import path, include
from clientes import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),
    path('', include('fornecedores.urls')),
]