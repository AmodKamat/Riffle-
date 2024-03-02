from django.shortcuts import render,redirect
import re
from customusermodel.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import time
# Create your views here.
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
import random
import string
def login_required_redirect(to_url):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                # User is logged in, redirect to the specified URL
                return redirect(to_url)
            else:
                # User is not logged in, proceed with the original view
                return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
def generate_unique_email_token(length):
    User = get_user_model()
    
    while True:
        characters = string.ascii_letters + string.digits + '-_'
        random_string = ''.join(random.choice(characters) for _ in range(length))
        if not User.objects.filter(email_token=random_string).exists():
            return random_string
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def send_html_email(subject, to_email, html_content):
    email = EmailMultiAlternatives(
        subject=subject,
        body=strip_tags(html_content),
        to=[to_email],
    )

    email.attach_alternative(html_content, 'text/html')

    email.send()
def get_user_by_username(username):
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None
def is_username_taken(username):
     return User.objects.filter(username=username).exists()
def is_email_taken(email):
    return User.objects.filter(email=email).exists() 
def is_email(s):
         email_pattern = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
         return bool(email_pattern.match(s))
def get_username_from_email(email):
          try:
           user = User.objects.get(email=email)
           return user.username
          except User.DoesNotExist:
           return None   
       
@login_required_redirect(to_url='homepage')     
def register(request):
    context = 'success'
    reversed_numbers = reversed(range(1, 4))
    data = {'context': context, 'reversed_numbers': list(reversed_numbers)}
    if request.method == 'POST':
       
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ';', ':', ',', '.', '<', '>', '?', '/', '|', '\\']
        username = request.POST.get('username').lower()
        email =request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        print(username,email,password,confirmpassword)
        if not is_email(email):
         print('Invalid email format')
         return render(request, 'registration.html')
        elif not password:
            print('Password cannot be empty')
            return render(request, 'registration.html')
        elif not confirmpassword:
            print('Please confirm your password')
            return render(request, 'registration.html')
        elif is_username_taken(username):
            print('Username is already taken')
            return render(request, 'registration.html')
        elif is_email_taken(email):
            print('Email is already registered')
            return render(request, 'registration.html')
        else:
         print('registerdone')
         newuser = User.objects.create_user(username,email,password)
         newuser.email_token = generate_unique_email_token(100)
         print(newuser.email_token)
         subject = 'Riffle Account activation'
         to_email = f'{email}'
         activation_link = f'http://127.0.0.1:8000/activation/{username}/{newuser.email_token}'
         css = """
<style>
    body {
      background: #FBFBFD;
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
    }

    .container {
      background: #d5d5f8;
      padding: 20px;
      border-radius: 10px;
      margin: 20px auto;
      max-width: 600px;
    }

    #logo {
      display: block;
      margin: 0 auto;
    }

    h2 {
      color: #7D4EF5;
      text-align: center;
    }

    p {
      color: #0B0910;
      text-align: center;
      line-height: 1.6;
    }

    .activate-btn {
      display: block;
      width: 100%;
      background: #461AB8;
      color: #EAE6F3;
      text-decoration: none;
      padding: 10px;
      border-radius: 5px;
      text-align: center;
      margin-top: 20px;
    }

    .footer {
      margin-top: 20px;
      text-align: center;
      color: #A489EA;
    }
</style>
"""

         html_content = f"""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Riffle - A New Social Experience</title>
  {css}
</head>

<body>
  <div class="container">
    <img style="width:100%" src="https://lh3.googleusercontent.com/u/3/drive-viewer/AEYmBYQdFLEH21jWihiHyDLSHvBclzJKxDx4MjQQ5Mm3zi6mrNEhyoSLctB-Fmy7vreO7Q918M8rTJGtiAGf8o6lGdD2NaUkJQ=w1920-h988" alt="Riffle Logo" id="logo">
    <h2>Welcome to Riffle - A New Social Experience!</h2>
    <p>Riffle is where conversations come alive. Connect with old friends, make new ones, and explore a world of shared interests.</p>
    <a href="{activation_link}" class="activate-btn">Activate Your Riffle Account.This link will only work once</a>
    <p>Why Choose Riffle?</p>
    <ul>
      <li>Dynamic Feeds: Stay updated with the latest posts and stories from your network.</li>
      <li>Interactive Chats: Engage in lively group chats and private conversations.</li>
      <li>Privacy First: We prioritize your data security and privacy.</li>
      <li>Personalized Experience: Tailor your profile and preferences to reflect your personality.</li>
    </ul>
    <p>Click the button above to activate your Riffle account and embark on a unique social journey!</p>
  </div>
  <div class="footer">
    <p>Thank you for joining Riffle! For more details and updates, visit <a href="https://www.riffle.com">www.riffle.com</a></p>
  </div>
</body>

</html>
"""
 
         send_html_email(subject, to_email, html_content)
         newuser.save()     
         return render(request,'registration.html',{'context':context})
         
         
         
            
    return render(request,'registration.html')

@login_required_redirect(to_url='homepage')     

def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        if is_email(username_or_email):
            username_or_email = get_username_from_email(username_or_email)

        activation_check = get_user_by_username(username_or_email)
        if activation_check is not None:
          user = authenticate(username=username_or_email, password=password)
          if user is not None and activation_check.email_activated:
              login(request, user)
              print('logged')
              return redirect('homepage')
          elif user is not None :
            subject = 'Tickr Account activation'
            to_email = f'{user.email}'
            activation_link = f'http://127.0.0.1:8000/activation/{user.username}/{user.email_token}'
            css = """<style>
    body {
      background: #FBFBFD;
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
    }

    .container {
      background: #d5d5f8;
      padding: 20px;
      border-radius: 10px;
      margin: 20px auto;
      max-width: 600px;
    }

    #logo {
      display: block;
      margin: 0 auto;
    }

    h2 {
      color: #7D4EF5;
      text-align: center;
    }

    p {
      color: #0B0910;
      text-align: center;
      line-height: 1.6;
    }

    .activate-btn {
      display: block;
      width: 100%;
      background: #461AB8;
      color: #EAE6F3;
      text-decoration: none;
      padding: 10px;
      border-radius: 5px;
      text-align: center;
      margin-top: 20px;
    }

    .footer {
      margin-top: 20px;
      text-align: center;
      color: #A489EA;
    }
  </style>"""
            html_content = f"""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Riffle - A New Social Experience</title>
  {css}
</head>

<body>
  <div class="container">
    <img style="width:100%" src="https://lh3.googleusercontent.com/u/3/drive-viewer/AEYmBYQdFLEH21jWihiHyDLSHvBclzJKxDx4MjQQ5Mm3zi6mrNEhyoSLctB-Fmy7vreO7Q918M8rTJGtiAGf8o6lGdD2NaUkJQ=w1920-h988" alt="Riffle Logo" id="logo">
    <h2>Welcome to Riffle - A New Social Experience!</h2>
    <p>Riffle is where conversations come alive. Connect with old friends, make new ones, and explore a world of shared interests.</p>
    <a href="{activation_link}" class="activate-btn">Activate Your Riffle Account.This link will only work once</a>
    <p>Why Choose Riffle?</p>
    <ul>
      <li>Dynamic Feeds: Stay updated with the latest posts and stories from your network.</li>
      <li>Interactive Chats: Engage in lively group chats and private conversations.</li>
      <li>Privacy First: We prioritize your data security and privacy.</li>
      <li>Personalized Experience: Tailor your profile and preferences to reflect your personality.</li>
    </ul>
    <p>Click the button above to activate your Riffle account and embark on a unique social journey!</p>
  </div>
  <div class="footer">
    <p>Thank you for joining Riffle! For more details and updates, visit <a href="https://www.riffle.com">www.riffle.com</a></p>
  </div>
</body>

</html>
"""
            send_html_email(subject, to_email, html_content)
            context='sent'
            print('activate' if not activation_check.email_activated else 'bad')
            return render(request, 'login.html', {'context': context})
        else:
            print('bad')
            context = 'bad'
            return render(request, 'login.html', {'context': context})

    return render(request, 'login.html')

   


                  
@login_required_redirect(to_url='homepage')              
def activation(request,username,uniqueid):
    user = get_user_by_username(username)
    print('ok')
    print(uniqueid)
    if user.email_token == uniqueid:
        print('ok2')
          
        user.email_token = generate_unique_email_token(100)
        user.email_activated=True
        user.save()
        return render(request,'activation.html')
    elif user.email_token != uniqueid:
        return HttpResponse('hgffnhgfnjf')
    else:
        return redirect('register')   
        

def user_logout(request):
  user = request.user
  if user.is_authenticated:
    logout(request)
    return redirect('homepage')
  return redirect('homepage')  