from django.contrib import admin # type: ignore

# Register your models here.
from .models import Job

admin.site.register(Job)
