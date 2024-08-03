from django.db import models # type: ignore

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100) # Column
    
    
    # image = models.ImageField(upload_to='images/')
    # summary = models.CharField(max_length=200)
    # title = models.CharField(max_length=200)
    # url = models.CharField(max_length=200)
    # def __str__(self):
    #     return self.title
