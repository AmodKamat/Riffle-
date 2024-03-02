from django.db import models
from customusermodel.models import User

class Post(models.Model):

    post_user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True ,verbose_name='User')
    description = models.CharField(max_length=100, verbose_name='Post Description')
    image = models.ImageField(max_length=500,upload_to='Post', verbose_name='Image')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creation Timestamp')
    updated_at = models.DateField(auto_now=True, verbose_name='Last Updated Timestamp')
    likes = models.ManyToManyField(User,related_name='socialmedia.Like.posts+',blank=True,null=True)
    def like_count(self):
        return self.like_set.count()
   
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='Related Post')
    Commenting_user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True ,verbose_name='Commenting User')
    description = models.CharField(max_length=100, verbose_name='Comment Content')
    created_at = models.DateField(auto_now_add=True, verbose_name='Comment Creation Timestamp')
    updated_at = models.DateField(auto_now=True, verbose_name='Last Comment Update Timestamp')


class FAQ(models.Model):
    question = models.CharField(max_length=50, verbose_name='FAQ Question')
    answer = models.CharField(max_length=350, verbose_name='FAQ Answer')
    created_at = models.DateField(auto_now_add=True, verbose_name='FAQ Creation Timestamp')
    updated_at = models.DateField(auto_now=True, verbose_name='Last FAQ Update Timestamp')