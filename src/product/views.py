from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, RedirectView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User  # Asegúrate de importar User si lo vas a usar
from .models import Product, DigitalProduct  # Asegúrate de importar tus modelos correctamente
from django.http import HttpResponseRedirect
from .mixins import TemplateTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductModelForm  # Asegúrate de importar tu formulario si lo vas a usar


class ProtectedListView(LoginRequiredMixin, TemplateTitleMixin, ListView):
    model = Product
    template_name = 'product/product_list.html'
    title = 'Mis Productos Personalizados'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class DigitalProductListView(TemplateTitleMixin,ListView):
    model = DigitalProduct
    template_name = 'product/product_list.html'  # Asegúrate que este template exista
    title = 'Productos Digitales'


class ProductListView(TemplateTitleMixin, ListView):
    #app_label = 'product'  # Asegúrate de que este sea el nombre correcto de tu aplicación
    #model = Product  # Define el modelo que se usará para esta vista
    #view_name = 'product_list'  # Nombre de la vista para referenciar en URLs
    #template_name = '<app_name>/<model>_<view_name>.html'  # Define el template a usar
    #template_name = 'product/product_list.html'  # Asegúrate que este template exista
    model = Product
    title = 'Productos Físicos'
    
class DetailView(DetailView):
    model = Product
    
class ProductIDRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        pk = url_params.get('pk')
        obj = get_object_or_404(Product, pk=pk)
        slug = obj.slug
        return f'/product/products/{slug}/'

class ProductRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        slug = url_params.get('slug')
        return f'/product/products/{slug}/'

class ProtectedProductDetailView(LoginRequiredMixin, DetailView):
    model = Product



class ProtectedProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductModelForm
    template_name = 'forms.html'  # Asegúrate que este template

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)


class ProtectedProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductModelForm
    template_name = 'product/product_detail.html'  # Asegúrate que este template exista

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    def get_success_url(self):
        return self.object.get_edit_url()

class ProtectedProductDeleteView(LoginRequiredMixin, DeleteView):

    template_name = 'forms-delete.html'  # Asegúrate que este template exista

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return '/product/products/'  # Redirige a la lista de productos después de eliminar

# def about_us_redirect_view(request):
#     return HttpResponseRedirect("/about/")
# def team_redirect_view(request):
#     return HttpResponseRedirect("/team/")  # Redirige a la vista de 'about'


# # Vista basada en función
# def product_list_view(request):
#     if request.method == 'POST':
#         print(request.POST)
#     return render(request, 'products/lista.html', {})  # Asegúrate que este template exista

# # Vista basada en clase simple
# class ProductHomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'products/home.html', {})

#     def post(self, request, *args, **kwargs):
#         print(request.POST)
#         return render(request, 'products/home.html', {})

# # Vista basada en clase usando ListView para productos
# class ProductListView(ListView):
#     queryset = Product.objects.all()
#     template_name = 'products/lista.html'  # Define el template a usar

# # Vista basada en clase para listar posts del blog
# class BlogPostListView(ListView):
#     queryset = Post.objects.all()
#     template_name = 'blog/lista.html'

# # Vista basada en clase para listar usuarios y sus posts (si aplica)
# class UsersPostListView(ListView):
#     queryset = User.objects.all()
#     template_name = 'users/lista.html'