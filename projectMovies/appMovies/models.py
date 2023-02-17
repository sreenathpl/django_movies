from django.db import models

# Create your models here.
class model_movies(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='images')
    cat = models.CharField(max_length=50)
    duration = models.CharField(max_length=10)
    director = models.CharField(max_length=150)

    def __str__(self):
        return self.name