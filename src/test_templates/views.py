from django.shortcuts import render
from django.contrib import messages

from datetime import datetime

# Create your views here.
def test_view(request):
    my_List = ['Mouse',
               'Teclado',
               'Celular',
               'Computador',
               'Laptop',
               'Lapiz',
               'Maleta']
    context = {
        'view_title':'Mi Titulo increible',
        'my_number':635,
        'my_number2':2000,
        'today': datetime.now().today(),
        'my_List':my_List
    }
    #template = 'test_templates/test-view.html'
    template = 'test_templates/detail-view.html' #<----------------

    messages.add_message(request, messages.INFO, 'Mensaje de prueba 1')
    messages.add_message(request, messages.INFO, 'Mensaje de prueba 2')

    return render(request, template, context)