from django.shortcuts import render
from django.forms import formset_factory, modelformset_factory


# Create your views here.

from .forms import TestForm
from .forms import ProductModelForm
from .models import Product


def home(request):
    ProductModelFormSet = modelformset_factory(Product, form=ProductModelForm)
    formset = ProductModelFormSet(request.POST or None, queryset=Product.objects.all())

    print('formset.data')
    print(formset.data)

    print('formset.errors')
    print(formset.errors)

    formset.clean()
    if formset.is_valid():
        print('ModelFormset es valido')
        formset.save()






    # TestFormSet = formset_factory(TestForm, extra=3)

    # if request.method == 'POST':
    #     formset = TestFormSet(request.POST)
    #     if formset.is_valid():
    #         for form in formset:
    #             print(form.cleaned_data)
    # else:
    #     formset = TestFormSet()  # Aquí se generan los formularios con valores por defecto

    context = {
        'formset': formset
    }
    return render(request, 'formset_view.html', context)
