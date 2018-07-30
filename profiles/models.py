import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.id


def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_user_profile, sender=User)
