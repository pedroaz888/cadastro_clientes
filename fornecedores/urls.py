from django.contrib import admin
from django.urls import path
from fornecedores import views

urlpatterns = [

    path('cadastro_fornecedores/', views.cadastro_fornecedores, name='cadastro_fornecedores'),
    path('lista_fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('excluir_fornecedor/<int:id>/', views.excluir_fornecedor, name='excluir_fornecedor'),
    path('buscar_servico_e_produtos', views.buscar_servico_e_produtos, name='buscar_servico_e_produtos'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

   