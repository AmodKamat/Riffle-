from django.urls import path
from . import views
urlpatterns = [
    path('editprofile',views.editprofile,name='editprofile'),
    path('posts',views.posts,name='posts'),
    path('liked/<int:id>',views.liked,name='like-post'),
    path('comment/<int:post_id>',views.add_comment,name='add-comment'),
    path('add_post',views.add_post,name='addpost')
]
