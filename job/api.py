from .models import Job
from .Serializers import JobSerializer
from rest_framework.response import Response


def job_list_api(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

