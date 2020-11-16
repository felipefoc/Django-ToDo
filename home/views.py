from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Task

# Create your views here.

@login_required
def homePage(request):
    all_tasks = Task.objects.all().filter(user=request.user)
    context = {'tasks': all_tasks}
    return render(request, 'home.html', context) 