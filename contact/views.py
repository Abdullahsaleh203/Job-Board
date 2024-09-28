from django.shortcuts import render

# Create your views here.
def send_message(request):
    return render(request,'contact/contact.html',{})

