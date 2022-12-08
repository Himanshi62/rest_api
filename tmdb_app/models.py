from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    description = models.TextField()
    release_date = models.CharField(max_length = 100)
    isHit = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
        