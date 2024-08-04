from django.shortcuts import render
from .models import Job
# Create your views here.
def jobs_list(request):
    jobs_list=Job.objects.all() # get all jobs from database
    # return render(request , 'job/jobs_list.html')
    pass


def jobs_detali(request,id):
    # return render(request , 'job/jobs_detali.html')
    pass
