from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Achievment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title