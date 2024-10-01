# get the data from the database and convert it into JSON format
from rest_framework import serializers
from .models import Job

# Serializers define the API representation.
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
