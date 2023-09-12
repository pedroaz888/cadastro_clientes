
from django.contrib import admin
from django.urls import path
from clientes import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('buscar_nomes/', views.buscar_nomes, name='buscar_nomes'),
    path('home/', views.home, name='home'),
    path('lista/', views.lista, name='lista'),
    path('excluir_cliente/<int:id>/', views.excluir_cliente, name='excluir_cliente'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
