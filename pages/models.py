from django.conf import settings
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

class Article(models.Model):
    custom_author_id = CustomUser.id

    image = models.ImageField(upload_to='images/', default='/images/algo-logo.png')
    title = models.CharField(max_length=200)
    author = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')