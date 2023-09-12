from .models import Clientes
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages  

def home(request):
    if request.method == "POST":
        apelido = request.POST.get('apelido')
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        
       
        if apelido and nome and telefone and email:
            cliente = Clientes(apelido=apelido, nome=nome, telefone=telefone, email=email)
            cliente.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente registrado com sucesso.')
            
        else:
            messages.add_message(request, messages.WARNING, 'Preencha os dados corretamente.')

        return redirect('home') 
       
    return render(request, 'home.html')


def lista(request):
    if request.method == "GET":
        id = request.GET.get('id')
        apelido = request.GET.get('apelido')
        nome = request.GET.get('nome')
        telefone = request.GET.get('telefone')
        email = request.GET.get('email')

        # Filtrar clientes com base nos parâmetros de consulta
        clientes = Clientes.objects.all()

    if id:
        clientes = clientes.filter(id__icontains=id)
    if apelido:
        clientes = clientes.filter(apelido__icontains=apelido)
    if nome:
        clientes = clientes.filter(nome__icontains=nome)
    if telefone:
        clientes = clientes.filter(telefone=telefone)
    if email:
        clientes = clientes.filter(email__icontains=email)

    return render(request, 'lista.html', {'clientes': clientes})


def buscar_nomes(request):
 
    query = request.GET.get('buscar_nomes')

    if query:
        buscar_nomes = Clientes.objects.filter(nome__icontains=query)
        if not buscar_nomes:
            messages.warning(request, 'Cliente ainda não registrado.')     
    else:
        buscar_nomes = Clientes.objects.all()
       
    return render(request, 'lista.html', {'clientes': buscar_nomes})

def excluir_cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()

    messages.error(request, 'Cliente excluído com sucesso.')  
  
    return redirect('lista')





