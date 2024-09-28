from django.urls import path ,include 
from . import views
app_name='contact'


urlpatterns = [
    path('',views.send_message ,name='contact'),
]
