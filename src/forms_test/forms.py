from django import forms

YEARS = [x for x in range(1900,2030)]
MY_CHOICES = [
    ("db-value1", "Opcion 1"),
    ("db-value2", 'Opcion 2')

]

from .models import Product

class ProductModelForm (forms.ModelForm):
    labels = {
        'title':'Mi etiqueta para el titulo',
        'slug':'Mi etiqueta para el slug',
        'price': 'Mi etiqueta para el precio',
    }
    class Meta:
        model = Product
        fields = [
        'title',
        'slug',
        'price'
        ]
        exclude = []
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if len(title) <= 10:
            raise forms.ValidationError('El titulo debe ser mayor a 10 caracteres')
        return title
    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get('slug')
        if len(slug) <= 10:
            raise forms.ValidationError('El slug debe ser mayor a 10 caracteres')
        # if " " in slug:
        #     raise forms.ValidationError('El slug no puede contener espacios, te recomendamos usar - para sustituirlo')
        if "miMarca" not in slug:
            raise forms.ValidationError('El slug debe incluir miMarca')
        return slug

class TestForm(forms.Form):
    fecha = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    un_texto = forms.CharField(label='Ingresa un texto:', widget=forms.Textarea(attrs={'rows':4, 'cols':15}))
    boolean = forms.BooleanField()
    entero = forms.IntegerField()
    email = forms.EmailField()
    opciones = forms.CharField(label='Selecciona una opcion', widget=forms.Select(choices=MY_CHOICES))
    opciones_radio = forms.CharField(label='Selecciona una opcion', widget=forms.RadioSelect(choices=MY_CHOICES))
    opciones_checkbox = forms.CharField(label='Selecciona una opcion', widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES))

    def clean_entero(self, *args, **kwargs):
        entero = self.cleaned_data.get("entero")
        if entero > 100:
            raise forms.ValidationError('El entero debe ser menor  o igual que 100')
        return entero
    
    def clean_un_texto(self, *args, **kwargs):
        un_texto = self.cleaned_data.get('un_texto')
        if len(un_texto) < 10:
            raise forms.ValidationError('El texto debe contener más de 10 caracteres')
        return un_texto
    
        
