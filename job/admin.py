from django.contrib import admin # type: ignore

# Register your models here.
from .models import Job , Category

admin.site.register(Job)
admin.site.register(Category)
