from django.urls import path , include

from . import views


urlpatterns = [
    path('' , views.jobs_list , name='jobs_list'),
    path('<int:id>' , views.jobs_detali , name='jobs_detali'),
]
