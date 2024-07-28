from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    kind = models.CharField(max_length=200, choices= [('1', 'worker'), ('2', 'supervisor')], default=1)

    def __str__(self):
        return f'{self.user.username} Profile'



class Room(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='rooms/', null=True, blank=True, default='default.jpg')

    def __str__(self): 
        return self.name
    
class Task(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='tasks/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Assign(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done_at = models.DateTimeField(auto_now_add=True)
    supervisor_approved = models.BooleanField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-done_at']

    def save(self, *args, **kwargs):
        if self.task:
            self.task_name = self.task.name
            self.room_name = self.task.room.name
        super().save(*args, **kwargs)


    def __str__(self):
        return self.user.username