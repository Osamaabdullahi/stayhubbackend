from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Profile

# Signal to create Profile when a new CustomUser is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to save the Profile when CustomUser is saved
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
