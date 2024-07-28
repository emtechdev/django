from django import forms
from django.contrib.auth.models import User
from . models import Room, Task, Assign, Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    kind = forms.ChoiceField(choices=[(1, 'worker'), (2, 'supervisor')], required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username',  'password1', 'password2', 'kind', 'image']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile(user=user, kind=self.cleaned_data['kind'])
            if self.cleaned_data['image']:
                profile.image = self.cleaned_data['image']
            profile.save()
        return user


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
        
class AssignUpdateForm(forms.ModelForm):
    class Meta:
        model = Assign
        fields = ['supervisor_approved', 'comment']
        widgets={
   
         'comment':forms.Textarea(attrs={
            'class': 'block w-full rounded-md mt-2 mb-2 bg-white p-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50'
        })
    }