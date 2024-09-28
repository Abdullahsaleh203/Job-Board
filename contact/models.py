from django.db import models

# Create your models here.
class Info(models.Model):
    place = models.CharField(max_length=50)
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone_number = models.CharField(max_length=20)
    class Meta:
        verbose_name = ("Contact Information")
        verbose_name_plural = ("Contact Information")
        
    def __str__(self):
        return self.email
