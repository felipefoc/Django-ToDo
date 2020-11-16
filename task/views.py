from django.shortcuts import render, redirect
from .forms import TaskForm
from account.models import Task
import sweetify as swal


# Create your views here.
def add_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(request.user.id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            swal.success(request, title='Task criada')
            response = redirect('/home')
            return response

    context = {'form': form}
    return render(request, 'add_task.html', context)


def remove_task(request, pk=None):
    if pk:
        task = Task.objects.get(pk=pk)
        task.delete()
        response = redirect('/home')
        return response