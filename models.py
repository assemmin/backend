from django.db import models
class Movie(models.Model):
    title = models.CharField(max_length=255)
    descriptoin = models.TextField()
    producer = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
# Create your models here.
