from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from account.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'tasktext']
        labels = { 'name' : 'Nome :',
                    'tasktext' : 'Tarefa :',
                 }
        name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
        'placeholder':'Nome'}))
        tasktext = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
        'placeholder':'Tarefa'}))
