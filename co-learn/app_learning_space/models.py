from django.db import models
from app_profile.models import Profile

class LearningSpace(models.Model):
    name = models.CharField(max_length="64")
    colearners = models.ManyToManyField(Profile)
    description = models.TextField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.name
