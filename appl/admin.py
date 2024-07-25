from django.contrib import admin
from .models import  Room, Task, Assign
# Register your models here.


admin.site.register(Room)
admin.site.register(Task)

class AssignAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'done_at', 'supervisor_approved', 'comment')
    search_fields = ('task__name', 'user__username', 'comment')
    list_filter = ('supervisor_approved', 'done_at')

admin.site.register(Assign, AssignAdmin)