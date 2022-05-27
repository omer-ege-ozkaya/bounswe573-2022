from django.db import models
from app_profile.models import Profile
from app_learning_space.models import LearningSpace


class Article(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    like_count = models.IntegerField()
    learning_space = models.ForeignKey(LearningSpace, on_delete=models.CASCADE)