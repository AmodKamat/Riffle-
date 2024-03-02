from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email_token = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name='Email Token')
    dob = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    
    GENDER_CHOICES = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('others', 'Others'),
    )
    gender = models.CharField(max_length=20,blank=True, choices=GENDER_CHOICES, null=True, verbose_name='Gender')
    
    profile_pic = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Profile Picture')
    bio = models.CharField(max_length=100, null=True, blank=True, verbose_name='Bio')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='City')
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name='Country') 
    last_logout_time = models.DateTimeField(null=True, blank=True, verbose_name='Last Logout Time')
    is_online = models.BooleanField(default=False, verbose_name='Is Online')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creation Date')
    updated_at = models.DateField(auto_now=True, verbose_name='Last Update Date')
    email_activated = models.BooleanField(default=False, verbose_name='Email Activated')
    groups = models.ManyToManyField(Group,null=True ,blank=True, related_name='customuser_groups')
    is_completed = models.BooleanField(default=False,verbose_name = 'iscompleted' )
    user_permissions = models.ManyToManyField(Permission,null=True ,blank=True, related_name='customuser_user_permissions')
    def __str__(self):
        return self.username





