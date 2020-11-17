from account.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from datetime import datetime



# Create your views here.

@login_required
def homePage(request):
    all_tasks = Task.objects.filter(user=request.user, is_active=True)
    context = {'tasks': all_tasks}
    return render(request, 'home.html', context)


@login_required
def aboutPage(request):
    return render(request, 'about.html')

