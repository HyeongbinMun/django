from django.db import models

# Create your models here.
class Game(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    files = models.FileField(upload_to='file', blank=True, null=True)

    def __str__(self):
        return self.subject

class Game_images(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank = True, null = True)

class Category(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)