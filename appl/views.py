from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import  ListView,   DetailView, TemplateView, FormView, CreateView
from django.urls import reverse_lazy
from .models import Room, Task, Assign
from .forms import TaskForm, EditRoomForm, UserRegisterForm, AssignUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'user_list.html'


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
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')



class RoomView(TemplateView):
    template_name = 'room.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()

        return context
    

class HomeView(TemplateView):
    template_name = 'home.html'
       


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
    
    def post(self, request, *args, **kwargs):


        room = self.get_object()
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        assign = Assign(task=task, user=request.user)
        assign.save()
        return redirect('room_detail', pk=room.id)
    
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
                return redirect('room_detail', pk=room.pk)  
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



def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    room_pk = task.room.pk
    task.delete()
    return redirect('room_detail', pk=room_pk)



def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)

    if request.method == 'POST':
        form = EditRoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            submit_action = request.POST.get('submit_action')
            if submit_action == 'submit':
                return redirect('home')

    else:
        form = EditRoomForm(instance=room)
    
    return render(request, 'room_form.html', {
        'form': form, 
        'title': 'Edit room'
    })



def supervisor_approve(request, pk):
    room = get_object_or_404(Room, pk=pk)

    if request.method == 'POST':
        form = EditRoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            submit_action = request.POST.get('submit_action')
            if submit_action == 'submit':
                return redirect('home')

    else:
        form = EditRoomForm(instance=room)
    
    return render(request, 'room_form.html', {
        'form': form, 
        'title': 'Edit room'
    })


class AssignListView(ListView):
    model = Assign
    template_name = 'assign_list.html'
    context_object_name = 'assigns'

    def get_queryset(self):
        return Assign.objects.select_related('task__room', 'user').all()
    


def assign_update_view(request, pk):
    assign = get_object_or_404(Assign, pk=pk)

    if request.method == 'POST':
        form = AssignUpdateForm(request.POST, instance=assign)
        if form.is_valid():
            form.save()
            return redirect('assign_list')  
    else:
        form = AssignUpdateForm(instance=assign)

    return render(request, 'assign_update.html', {'form': form})