from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.HomeView.as_view(), name='home'),
    path('addtask/<int:pk>/', views.task_form_view, name='add_task'),
    path('room_detail/<int:pk>/', views.DetailView.as_view(), name='room_detail'),



]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
