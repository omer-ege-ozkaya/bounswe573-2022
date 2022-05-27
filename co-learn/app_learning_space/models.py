from django.db import models


class LearningSpace(models.Model):
    name = models.CharField(max_length="64")
    colearners = models.ManyToManyField("User")
    description = models.TextField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.name
    