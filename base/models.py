from email.policy import default
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo-home')