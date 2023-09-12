from django.contrib import admin
from django.urls import path
from fornecedores import views

urlpatterns = [

    path('cadastro_fornecedores/', views.cadastro_fornecedores, name='cadastro_fornecedores'),
    path('lista_fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('excluir_fornecedor/<int:id>/', views.excluir_fornecedor, name='excluir_fornecedor'),
    path('buscar_servico_e_produtos', views.buscar_servico_e_produtos, name='buscar_servico_e_produtos'),

]

   