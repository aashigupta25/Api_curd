from django.db import models

# Create your models here.
class APIoperation(models.Model):
    create = models.CharField(max_length = 100)    
    update = models.CharField(max_length = 100)
    retrieve = models.CharField(max_length = 100)
    delete = models.CharField(max_length = 100)
    

