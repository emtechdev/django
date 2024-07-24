from django import forms
from django.contrib.auth.models import User
from . models import Room, Task, Assign

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'arabic_name', 'description',  'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'arabic_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            

        }