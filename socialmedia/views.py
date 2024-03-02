from django.shortcuts import render, redirect
from django import forms
from customusermodel.models import User
from socialmedia.models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def data(request):
    lastfeed=None
    if request.user.is_authenticated:
        myposts = Post.objects.filter(post_user=request.user)
        count=myposts.count()
        if myposts:
            lastfeed=myposts[0].created_at
    else:
        count=lastfeed=0
    
    posts = Post.objects.all()
    comments=Comment.objects.all()
    context = {
        'posts': posts,
        'count': count,
        'lastfeed': lastfeed,
        'comments':comments
    }
    return context
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic', 'first_name', 'last_name', 'username']

    profile_pic = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'style': 'width:0px;height:0px; position:absolute;right:10000px',
                'id': 'profile-avatar',
                'class': 'profile-avatar-input',
                'accept': 'image/*'
            }
        ),
        required=False
    )

    first_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    last_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    username = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
class EditProfileFormCustom(forms.Form):
    profile_avatar = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'style': 'width:0px;height:0px; position:absolute;right:10000px',
            'id': 'profile-avatar',
            'class': 'profile-avatar-input',
            'accept': 'image/*'
        }),
        required=False
    )

    f_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    l_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    username = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
@login_required(login_url='login')
def editprofile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)

        # Print form errors to the console for debugging
        if not form.is_valid():
            print(form.errors)
            messages.error(request,'username taken')
            return render(request, 'edit_profile.html', {'form': form,'user':user})
            
        if form.is_valid():
            user.is_completed=True
            form.save()
            return redirect('homepage')
    else:
        print('gotelse')
        form = EditProfileForm(instance=user)
        return render(request, 'edit_profile.html', {'form': form,'user':user})
def posts(request):
    posts = Post.objects.all
    return render(request,'posts.html',{'posts':posts})
def get_post(id):
    try:
        post = Post.objects.get(id=id)
        return post
    except Post.DoesNotExist:
        return None
@login_required    
def liked(request,id):
    post = Post.objects.get(id=id)
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    context = data(request)
    return redirect('homepage')

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        comment_text = request.POST['comment']

        # Create and save the comment
        Comment.objects.create(Commenting_user=request.user, post=post, description=comment_text)
    context=data(request)
    # return render(request,'home.html',context)
    return redirect('homepage')



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image']
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_user = request.user
            post.save()
            return redirect('homepage')  # Assuming you have a URL named 'home'
    else:
        form = PostForm()
    
    return render(request, 'addpost.html', {'form': form})