from django.urls import path ,include 
from . import views
from . import api
app_name='job'


urlpatterns = [
    path('',views.job_list ,name='job_list'),
    path('add',views.add_job ,name='add_job'),
    path('<str:slug>',views.job_detail ,name='job_detail'),
    path('add',api.job_api_list ,name='job_api_list'),
]

# urlpatterns = [
#     path('',views.job_detail ),
#     path('<int:id>',views.job_list ),
# ]
