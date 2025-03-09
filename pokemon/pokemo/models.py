from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=400)
    image = models.URLField()
    
    def __str__(self):
        return self.name
