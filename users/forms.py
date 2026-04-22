from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Enter email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(
        label='Enter username',
        required=True,
        help_text='Enter your username',
        widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(
        label='Enter password',
        required=True,help_text='Password should not be small',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        label='Confirm password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))


    class Meta:
        model = User
        fields = ['email', 'username',]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Enter email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(
        label='Enter username',
        required=True,
        help_text='Enter your username',
        widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ['email', 'username',]

class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(label='Upload your profile picture',required=False, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['img', 'gender', 'email_notifications']


class ContactForm(forms.Form):
    theme = forms.CharField(
        label='Тема повіомлення',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Ваша пошта',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Текст повідомлення',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )