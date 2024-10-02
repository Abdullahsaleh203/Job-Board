# views
from .models import Job
from .Serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all()
    data = JobSerializer(jobs, many=True).data
    return Response({'data':data})

@api_view(['GET'])
def job_details_api(request,id):
    job_details = Job.objects.get(id=id)
    data = JobSerializer(job_details).data
    return Response({'data':data})


class JobListApi(generics.ListCreateAPIView):
    model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer
   

class JobDetailsApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'
