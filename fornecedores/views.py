from .models import Fornecedores
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages  

def cadastro_fornecedores(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        produto_e_servicos = request.POST.get('produto_e_servicos')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        
       
        if nome and produto_e_servicos and telefone and email:
            fornecedores = Fornecedores(nome=nome, produto_e_servicos=produto_e_servicos, telefone=telefone, email=email)
            fornecedores.save()
            messages.add_message(request, messages.SUCCESS, 'Fornecedor registrado com sucesso.')
            
        else:
            messages.add_message(request, messages.WARNING, 'Preencha os dados corretamente.')

        return redirect('cadastro_fornecedores') 
       
    return render(request, 'cadastro_fornecedores.html')

def lista_fornecedores(request):
    if request.method == "GET":
        id = request.GET.get('id')
        nome = request.GET.get('nome')
        produto_e_servicos = request.GET.get('produto_e_servicos')
        telefone = request.GET.get('telefone')
        email = request.GET.get('email')

        # Filtrar clientes com base nos parâmetros de consulta
        fornecedores = Fornecedores.objects.all()

    if id:
        fornecedores = fornecedores.filter(id__icontains=id)
    if nome:
        fornecedores = fornecedores.filter(nome__icontains=nome)
    if produto_e_servicos:
        fornecedores = fornecedores.filter(produto_e_servicos__icontains=produto_e_servicos)
    if telefone:
        fornecedores = fornecedores.filter(telefone=telefone)
    if email:
        fornecedores = fornecedores.filter(email__icontains=email)

    return render(request, 'lista_fornecedores.html', {'fornecedores': fornecedores})


def buscar_servico_e_produtos(request):
 
    query = request.GET.get('buscar_servico_e_produtos')

    if query:
        buscar_servico_e_produtos = Fornecedores.objects.filter(produto_e_servicos__icontains=query)
        if not buscar_servico_e_produtos:
            messages.warning(request, 'Fornecedor ainda não registrado...')     
    else:
        buscar_servico_e_produtos = Fornecedores.objects.all()
       
    return render(request, 'lista_fornecedores.html', {'fornecedores': buscar_servico_e_produtos})

def excluir_fornecedor(request, id):
    fornecedor = Fornecedores.objects.get(id=id)
    fornecedor.delete()

    messages.error(request, 'Fornecedor excluído com sucesso.')  
  
    return redirect('lista_fornecedores')

