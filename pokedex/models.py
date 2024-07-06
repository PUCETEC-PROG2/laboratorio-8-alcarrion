from django.db import models

class Pokemon (models.Model):
    name= models.CharField(max_length=30, null=False)
    type= models.CharField(max_length=30, null=False)
    weigth = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    
    def __str__(self) -> str:
        return self.name

