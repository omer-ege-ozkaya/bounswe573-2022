from django.db import models
from app_profile.models import Profile
import os, uuid


def get_upload_path(instance, filename):
    filename = f"{uuid.uuid1()}.{filename.split('.')[-1]}"
    return os.path.join("images", "learning_space", filename)


class LearningSpace(models.Model):
    name = models.CharField(max_length=64)
    colearners = models.ManyToManyField(Profile, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(blank=True, upload_to=get_upload_path)

    def __str__(self):
        return self.name
