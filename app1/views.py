from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form': form, 'name': 'PERICLES'}
    return render(request, 'register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'login.html', context)