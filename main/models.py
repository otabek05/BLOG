import uuid
from django.db import models

from django.contrib.auth.models import User


class Todo(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)  # OneToMany
    body = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return f'{self.owner} - {self.body[:50]}'
    