from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import  ListView,   DetailView, TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from .models import Room, Task, Assign
from .forms import TaskForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')



class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()

        return context
    

class DetailView(DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        room = self.get_object()

        tasks = Task.objects.filter(room=room)

        context['tasks'] = tasks

        return context
    

    
def task_form_view(request, pk):
    room = Room.objects.get(pk=pk) 

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.room = room
            task.save()
            
            submit_action = request.POST.get('submit_action')
            if submit_action == 'submit':
                return redirect('home')
            elif submit_action == 'submit and add task':
                return redirect('add_task', pk=room.pk)
            # else:
            #     return redirect('add_lessons', pk=chapter.pk)
        
    else:
        form = TaskForm()
    
    return render(request, 'task_form.html', {
        'form': form,
        'room': room, 
        'title': 'New task'
    })

