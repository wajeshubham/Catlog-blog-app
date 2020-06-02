from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from myApp.models import Post, Comment


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

