from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone




class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    image = models.ImageField(upload_to='post_image')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    comment_likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    def __str__(self):
        return f"{self.user.username}'s comment on {self.post.author}'s post"



