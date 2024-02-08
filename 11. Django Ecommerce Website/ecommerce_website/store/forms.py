from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm   #,AuthenticationForm
# from django.forms.widgets import PasswordInput, TextInput


        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        
# class LoginForm(AuthenticationForm):
    
#     username = forms.CharField(widget=TextInput())
#     password = forms.CharField(widget=PasswordInput())

    

