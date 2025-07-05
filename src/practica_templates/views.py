from django.shortcuts import render

def productos_view(request):
    productos = [
        {'nombre': 'Dobok profesional', 'precio': 59.99},
        {'nombre': 'Cinturón negro', 'precio': 14.99},
        {'nombre': 'Protector de pecho', 'precio': 39.50},
        {'nombre': 'Casco de combate', 'precio': 29.99},
        {'nombre': 'Guantes', 'precio': 19.99},
        {'nombre': 'Espinilleras', 'precio': 24.99},
    ]
    return render(request, 'practica_templates/productos.html', {'productos': productos})