from django.db import models
from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.user.__str__()


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#     profile = Profile(user=instance)
#     if created:
#         profile.save()
