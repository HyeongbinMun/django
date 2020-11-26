from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_game')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_game')
    files = models.FileField(upload_to='file', blank=True, null=True)

    def __str__(self):
        return self.subject

class Game_images(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank = True, null = True)

class Category(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

class Comment(models.Model):
   game = models.ForeignKey(Game, null=True, blank=True, on_delete=models.CASCADE)
   content = models.TextField()
   create_data = models.DateTimeField()
