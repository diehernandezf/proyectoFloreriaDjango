from django.shortcuts import render, redirect
from .models import *

import os
from django.conf import settings
# Create your views here.


def cargarInicio(request):
    productos = Producto.objects.all()
    categoria = Producto.objects.all()
    return render(request, "inicio.html",{"producto":productos,"categoria":categoria})



def cargarAgregarProducto(request):
    productos = Producto.objects.all()
    categoria = Producto.objects.all()
    return render(request,"agregarProducto.html",{"prod":productos,"cate":categoria})



def agregarProducto(request):
    #print("AGREGAR PRODUCTOS", request.POST)
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_imagen = request.FILES['txtImagen']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku, nombre = v_nombre, precio = v_precio,stock = v_stock, descripcion = v_descripcion, imagenUrl=v_imagen, categoria_id = v_categoria )
    
    return redirect('/agregarProducto')

def cargarEditarProducto(request,sku):
    prod = Producto.objects.get(sku = sku)
    return render(request,"editarProducto.html",{"prod":prod})

def editarProducto(request):

    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']


    try:
        v_imagen = request.FILES['txtImagen']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagenUrl))
        os.remove(ruta_imagen)
    except:
        v_imagen = productoBD.imagenUrl

    productoBD.nombre = v_nombre
    productoBD.precio = v_precio
    productoBD.stock = v_stock
    productoBD.descripcion = v_descripcion
    productoBD.imagenUrl = v_imagen
    
    productoBD.save()

    return redirect('/agregarProducto')

def eliminarProducto(request,codigo_producto):
    producto = Producto.objects.get(sku = codigo_producto)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagenUrl))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregarProducto')

def cargarLogin(request):
    return render(request, "login.html")

def cargarRegistro(request):
    return render(request, "registro.html")

def cargarAdministracionDeUsuarios(request):
    return render(request, "usuarios.html")