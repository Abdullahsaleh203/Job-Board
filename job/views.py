from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

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
    paginator = Paginator(job_list, 1) # Show 25 contacts per page.

    context= {'jobs':job_list} # template context name 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'job/job_list.html',context)


def job_detail(request,id) :
    job_detail=Job.objects.get(id=id)
    context= {'job':job_detail} # template context name
    return render(request,'job/job_details.html',context)
