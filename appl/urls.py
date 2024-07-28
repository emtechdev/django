from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import AssignListView, assign_update_view, TaskUpdateView, edit_profile

urlpatterns = [

    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('room/', views.RoomView.as_view(), name='room'),
    path('addtask/<int:pk>/', views.task_form_view, name='add_task'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('room_detail/<int:pk>/', views.DetailView.as_view(), name='room_detail'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),  
    path('edit_room/<int:pk>/',views.edit_room, name='edit_room'),
    path('assigns/', AssignListView.as_view(), name='assign_list'),
    path('assign/update/<int:pk>/', assign_update_view, name='assign_update'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('edit_profile/<int:pk>/', edit_profile, name='edit_profile'),




]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

