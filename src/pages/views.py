import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

class Conversion:
    def __init__(self):
        self.valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romano_entero(self, romano):
        total = 0
        prev_valor = 0

        for letra in reversed(romano):  # Procesamos de derecha a izquierda
            valor = self.valores.get(letra, 0)  # Obtenemos el valor del símbolo romano

            if valor < prev_valor:  # Si el valor actual es menor que el anterior, se resta
                total -= valor
            else:  # Si es mayor o igual, se suma
                total += valor
            
            prev_valor = valor  # Guardamos el valor anterior para la próxima iteración

        return total


def home(request):
    conversion = Conversion()
    numero_romano = "XI"  # 11
    resultado = conversion.romano_entero(numero_romano)

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + 'probando esto',
        "python_ver": os.environ["PYTHON_VERSION"] + 'Mas Cambios',
        "resultado": 'El resultado de ' + numero_romano + ' es: ' + str(resultado),
    }

    return render(request, "pages/home.html", context)
