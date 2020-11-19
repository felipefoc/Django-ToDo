from django.forms import ModelForm
from django import forms
from youtube.models import Youtube_file
from django.contrib.auth.models import User


class YouTubeForm(ModelForm):
    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
                            label='Cole a URL :', 
                            help_text='URL inválida')

    class Meta:
        model = Youtube_file
        fields = ['url']



class YouTube_add(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
                            label='Titulo :')
    thumbnail = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
                            label='Thumb :')
    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['title', 'thumbnail']