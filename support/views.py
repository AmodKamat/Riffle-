from django.shortcuts import render,redirect
from . models import Support
# Create your views here.

def contactus(request):
    user = request.user
    if request.method =='POST':
        subject = request.POST.get('subject')
        description = request.POST.get('message')
        new_request=Support.objects.create(topic=subject,description = description)
        if user.is_authenticated:
            new_request.user = user
        new_request.save()    
        return redirect('homepage')
    return render (request,'contact_us.html')
