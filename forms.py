from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                            'class': 'form-control'}))
    username = forms.CharField(label='Username', required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                            'class': 'form-control'}))

class Meta:
    model = User
    fields = ['Username', 'Email', 'Password', 'Password2']
    labels = {'email': 'Email'}
