import uuid
from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=50, blank=True)
    image_caption = models.TextField(blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.id

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, caption):
        self.update(caption=caption)

    @classmethod
    def get_image_by_id(cls, n):
        Image.objects.get(id=n)
