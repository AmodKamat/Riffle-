from django.shortcuts import render,redirect
from django.contrib import messages
from socialmedia.models import Post,Comment
from socialmedia.views import data
# Create your views here.
def homepage(request):
    user= request.user
    context = data(request)
    
    if user.is_authenticated and not user.is_completed:
     messages.error(request,'complete your profile')
     return redirect('editprofile')
    return render(request,'home_page.html',context)   

def aboutus(request):
    return render (request,'about_us.html')


