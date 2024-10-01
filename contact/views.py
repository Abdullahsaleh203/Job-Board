from django.shortcuts import render

from django.conf import settings
from .models import Info
from django.core.mail import send_mail

# Create your views here.
def send_message(request):
    myinfo = Info.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
        message_with_email = f"From: {email}\n\nMessage:\n{message}"
        send_mail(
                subject,
                message_with_email,
                email,
                [settings.EMAIL_HOST_USER],  
                fail_silently=False,
            )
            
    return render(request,'contact/contact.html',{'myinfo':myinfo})

