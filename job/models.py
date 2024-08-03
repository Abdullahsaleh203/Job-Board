from django.db import models # type: ignore




'''
Model field reference¶
https://docs.djangoproject.com/en/5.0/ref/models/fields/
'''
# Create your models here.
JOB_TYPE =(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100) # Column
    job_type = models.CharField(max_length=100 ,choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    
    # image = models.ImageField(upload_to='images/')
    # summary = models.CharField(max_length=200)
    # title = models.CharField(max_length=200)
    # url = models.CharField(max_length=200)
    # def __str__(self):
    #     return self.title
