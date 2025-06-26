from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product

from .forms import ProductForm
from .models import Product

from django.db.models import Q



def product_delete_view(request, product_id):
    instance = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        instance.delete()
        messages.success(request, 'Producto eliminado con exito')
        return HttpResponseRedirect('/ecommerce/')
    context = {
        'product': instance,
    }
    template = 'ecommerce/delete-view.html'
    return render(request, template, context)



def product_update_view(request, product_id=None):
    instance = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.save()
        messages.success(request, 'Producto actualizado con exito')
        return HttpResponseRedirect(f'/ecommerce/{instance.id}')
    context = {
        'form': form
    }
    template = 'ecommerce/update-view.html'
    return render(request, template, context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit= False)
        instance.save()
        messages.success(request, 'Producto creado con exito')
        return HttpResponseRedirect(f'/ecommerce/{instance.id}')
    context = {
        'form': form
    }
    template = 'ecommerce/create-view.html'
    return render(request, template, context)
# Create your views here.
def product_detail_view(request, product_id):
    instance = get_object_or_404(Product, id=product_id)
    context = {
        'product': instance,
    }
    template = 'ecommerce/detail-view.html'
    return render(request, template, context)

@login_required
def product_list_view(request):
   query = request.GET.get('q', None)
   queryset = Product.objects.all()
   if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query) |
            Q(seller__icontains=query) |
            Q(color__icontains=query) |
            Q(product_dimensions__icontains=query)
        )
   template = 'ecommerce/list-view.html'
   context = {
      'products': queryset,
   }

   if request.user.is_authenticated:
      template = 'ecommerce/list-view.html'
   else:
        template = 'ecommerce/list-view-public.html'
   return render(request, template, context)

@login_required
def login_required_view(request):
   queryset = Product.objects.all()
   template = 'ecommerce/list-view.html'
   context = {
      'products': queryset,
   }

   if request.user.is_authenticated:
      template = 'ecommerce/list-view.html'
   else:
        template = 'ecommerce/list-view-public.html'
   return render(request, template, context)

#------------------------------------------ Practica 55:
def agregar_al_carrito(request, product_id):
    carrito = request.session.get('carrito', {})
    carrito[str(product_id)] = carrito.get(str(product_id), 0) + 1
    request.session['carrito'] = carrito
    messages.success(request, 'Producto agregado al carrito')
    return HttpResponseRedirect('/ecommerce/carrito/')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    items = []
    total = 0
    for product_id, cantidad in carrito.items():
        producto = get_object_or_404(Product, id=product_id)
        subtotal = producto.price * cantidad
        total += subtotal
        items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
    context = {
        'items': items,
        'total': total
    }
    return render(request, 'ecommerce/carrito.html', context)

def eliminar_del_carrito(request, product_id):
    carrito = request.session.get('carrito', {})
    if str(product_id) in carrito:
        del carrito[str(product_id)]
    request.session['carrito'] = carrito
    messages.warning(request, 'Producto eliminado del carrito')
    return HttpResponseRedirect('/ecommerce/carrito/')

def procesar_pedido(request):
    request.session['carrito'] = {}
    messages.success(request, '¡Pedido procesado con éxito!')
    return render(request, 'ecommerce/pedido_exitoso.html')