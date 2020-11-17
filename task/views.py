from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from account.models import Task
import sweetify as swal
from datetime import datetime


# Create your views here.
@login_required
def add_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            swal.success(request, icon='success', title='Task criada com sucesso', timer=3000)
            response = redirect('/home')
            return response

    context = {'form': form}
    return render(request, 'add_task.html', context)


@login_required
def complete_task(request, pk=None):
    if pk:
        task = Task.objects.get(pk=pk)
        task.is_active = False
        task.save()
        swal.success(request, title='Finalizada', icon='success', timer=5000, persistent='Ok', html='Você concluiu a task <b>{}</b> em <b>{}</b> !'.format(task.name, task.ended_date.strftime("%d-%m-%Y ás %H:%M")))
        response = redirect('/home')
        return response


@login_required
def ended_tasks(request):
    all_tasks = Task.objects.filter(user=request.user, is_active=False)
    context = {'tasks': all_tasks}
    return render(request, 'tasks_complete.html', context) 


@login_required
def remove_task(request, pk=None):
    task = Task.objects.get(pk=pk)
    if task.is_active is False:
        task.delete()
        swal.error(request, title='Task excluida', icon='warning', timer=3000, text='Task foi excluida permanentemente.')
        response = redirect('/ended_tasks')
        return response
    else:
        pass


@login_required
def edit_task(request, pk=None):
    task = Task.objects.get(pk=pk) 
    form = TaskForm(instance=task)
    form_old_name = task.name
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            swal.success(request, 
            title='Editado',
            text='A tarefa "{}" foi editada !'.format(form_old_name),
            icon='info')
            return redirect('/home')
    context = {'form': form,
                'pk':pk}
    return render(request, 'edit_task.html', context)





