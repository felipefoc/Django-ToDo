from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'first_name', 'last_name']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
    'placeholder':'Usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
    'placeholder':'Senha'}))

