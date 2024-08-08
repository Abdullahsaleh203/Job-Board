from django.urls import path ,include 
from . import views
app_name='job'

urlpatterns = [
    path('',views.job_list ),
    path('<int:id>',views.job_detail ,name='job_detail'),
]
# urlpatterns = [
#     path('',views.job_detail ),
#     path('<int:id>',views.job_list ),
# ]
