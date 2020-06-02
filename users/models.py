from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            op_size = (300, 300)
            img.thumbnail(op_size)
            img.save(self.profile_pic.path)
