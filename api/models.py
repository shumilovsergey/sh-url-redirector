from django.db import models
from django.utils import timezone

class Urls(models.Model):
    name = models.CharField(max_length=56, unique=True)
    url = models.CharField(max_length=256, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['created']