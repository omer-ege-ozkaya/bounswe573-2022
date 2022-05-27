from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from app_profile.models import Profile


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    profile = Profile(user=instance)
    if created:
        profile.save()
