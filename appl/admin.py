from django.contrib import admin
from .models import  Room, Task, Assign
# Register your models here.


admin.site.register(Room)
admin.site.register(Task)
admin.site.register(Assign)