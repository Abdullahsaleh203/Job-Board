from django.db import models # type: ignore




'''
Model field reference¶
https://docs.djangoproject.com/en/5.0/ref/models/fields/
'''
# Create your models here.
'''
    Django models field
    -html widget 
    -validation
    -db size
'''
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

JOB_TYPE =(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100) # Column
    # location
    job_type = models.CharField(max_length=100 ,choices=JOB_TYPE)
    description= models.TextField(max_length=1000)
    published_at= models.DateTimeField(auto_now=True)
    Vacancy= models.IntegerField(default=1)
    salary= models.IntegerField(default=0)
    experience= models.IntegerField(default=0)
    category= models.ForeignKey('Category',on_delete=models.CASCADE)
    image= models.ImageField(upload_to=image_upload)
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name= models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    

