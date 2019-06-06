"""
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    email  = forms.EmailField(required=True)

    class meta:
        model = User
        field = ('first_name','last_name', 'username', 'email','password1', 'password2' )
        """