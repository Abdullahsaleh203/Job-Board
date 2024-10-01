# views
from .models import Job
from .Serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all()
    data = JobSerializer(jobs, many=True).data
    return Response({'data':data})


