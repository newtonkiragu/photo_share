import uuid
from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=50, blank=True)
    image_caption = models.TextField(blank=True)
    poster = models.ForeignKey(User)
