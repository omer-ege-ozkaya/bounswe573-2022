from django.db import models
from app_profile.models import Profile
from app_article.models import Article


class Post(models.Model):
    body = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.body[:50]
