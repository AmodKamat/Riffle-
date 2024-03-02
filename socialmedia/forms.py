# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from customusermodel.models import User

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic', 'first_name', 'last_name', 'username']
        widgets = {
            'profile_pic': forms.ClearableFileInput(attrs={
                'style': 'width:0px;height:0px; position:absolute;right:10000px',
                'id': 'profile-avatar',
                'class': 'profile-avatar-input',
                'accept': 'image/*'
            }),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }
class EditProfileForm(forms.Form):
    profile_avatar = forms.FileField(
        widget=forms.ClearableFileInput( attrs={
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
        widget=forms.TextInput(attrs={'placeholder': 'First Name','value':'namejo'})
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