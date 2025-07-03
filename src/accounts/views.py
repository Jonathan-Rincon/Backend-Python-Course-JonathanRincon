from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User

def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('/ecommerce/')
    return render(request, 'register.html', {'form': form})