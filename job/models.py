from django.db import models # type: ignore
from django.utils.text import slugify  # type: ignore



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
    
    slug = models.SlugField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    def save(self,*arg, **kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*arg, **kwargs)
class Category(models.Model):
    name= models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    

