# from typing_extensions import Required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# from typing_extensions import Required

class SignupForm(UserCreationForm):
    first_name=forms.CharField(max_length=25,help_text='Optional.')
    last_name=forms.CharField(max_length=25,help_text='Optional.')
    email=forms.EmailField(help_text='Required.Inform a valid email addres')
  
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )