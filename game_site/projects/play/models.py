from django.db import models

# Create your models here.
class Game(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Category(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)