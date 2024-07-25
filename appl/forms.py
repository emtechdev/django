from django import forms
from django.contrib.auth.models import User
from . models import Room, Task, Assign

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'arabic_name',   'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full rounded-md mt-2 border-0 p-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 sm:text-lg sm:leading-6'}),
            'arabic_name': forms.TextInput(attrs={'class': 'block w-full rounded-md mt-2 border-0 p-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 sm:text-lg sm:leading-6'}),
            'image': forms.FileInput(attrs={'class': 'block w-full rounded-md mt-2 bg-white p-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50'}),
            

        }

class EditRoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=( 'name',  'image')

        widgets={
       
         'name':forms.TextInput(attrs={
            'class': 'block w-full rounded-md mt-2 border-0 p-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 sm:text-lg sm:leading-6'
        }),
     
   
         'image':forms.FileInput(attrs={
            'class': 'block w-full rounded-md mt-2 bg-white p-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50'
        })
    }