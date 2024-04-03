from django.db import models

from users.models import CustomUser

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie,related_name='ratings', on_delete=models.CASCADE)
    rating = models.FloatField()
