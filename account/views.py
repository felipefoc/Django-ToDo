from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')


    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    form = LoginForm(request.POST)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Usuário ou senha incorretos')

    context = {'form' : form}
    return render(request, 'login.html', context)


@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')
