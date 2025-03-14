from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    image = models.URLField()
    abilities = models.TextField()  

    def get_abilities(self):
        """ Devuelve las habilidades como una lista """
        return self.abilities.split(",")  

    def __str__(self):
        return self.name






#from django.db import models

#class Pokemon(models.Model):
 #   name = models.CharField(max_length=400)
  #  image = models.URLField()
    
   # def __str__(self):
    #    return self.name
