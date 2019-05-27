from django.shortcuts import *
from django.http import request
from django.views.generic import *
from .models import Productos,Pago,Cliente,Compra
from django.urls import reverse_lazy
from .forms import ClienteForm


# Create your views here.
def res(request):
    productos = Productos.objects.all()
    return render(request,"croco/usuario.html",{ "Venta":productos })

def menu(request):
    return render(request,"croco/menu.html")

def shop(request):
    productos = Productos.objects.all()
    return render(request, "croco/tienda.html", {"Venta": productos})
    #return render(request,"croco/tienda.html")

def detalles(request,codigo):
    productos =Productos.objects.get(codigo=codigo)
    return render(request,"croco/usuario.html", {"Compra": productos})

def formulario(request,code):
    if request.method =='POST':
        form = ClienteForm(request.POST)
        productos = Productos.objects.get(codigo=code)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            #return redirect(pago,code=productos.codigo,cliente=cliente.id)
    else:
        productos=Productos.objects.get(codigo=code)
        form = ClienteForm()
    return render(request,'croco/formulario_usuario.html',{'form':form ,'objeto':productos})

def pago(request,code,user):
    productos = Productos.objects.get(codigo=code)
    cliente = get_object_or_404(Cliente,user)
    return render(request,'croco/pago.html',{'cliente':cliente, 'object':productos})


