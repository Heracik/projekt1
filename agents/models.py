from django.db import models
from django.contrib.auth.models import AbstractUser

class Agent(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    povod = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ability(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='abilities')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.agent.name})"
    
