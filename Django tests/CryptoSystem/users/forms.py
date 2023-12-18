from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'Last Name'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class':'input-field', 'placeholder':'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-field', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-field', 'placeholder':'Confirm Password'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('first_name','last_name','email')
        fields = ('first_name','last_name','email','username','password1','password2')

class CustomAuthenticationForm(AuthenticationForm):
    """
    Custom authentication form that accepts a different class.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-field', 'placeholder':'Password'}))