from django.shortcuts import render
from .models import Job

# Create your views here.

def job_list(request) :
    """
    View function for displaying a list of jobs.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML template displaying the list of jobs.
    context: A dictionary containing the job list
    """
    job_list=Job.objects.all()
    return render(request,'job/job_list.html',
                  {'job_list':job_list})
def job_detail(request,id) :
    pass
