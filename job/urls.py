from django.urls import path ,include 
from . import views

urlpatterns = [
    path('',views.job_detail ),
    path('<int:id>',views.job_list ),
]
