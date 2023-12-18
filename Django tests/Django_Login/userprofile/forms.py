from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    
#     password1 = forms.CharField(
#         label='Password',
#         widget=forms.PasswordInput(attrs={'class':'fa fa-eye-slash'}),
#         help_text='Your password must be at least 8 characters long, and must contain at least one uppercase letter, one lowercase letter, one number, and one special character.',
#     )

#     password2 = forms.CharField(
#         label='Password confirmation',
#         widget=forms.PasswordInput(attrs={'class':'fa fa-eye-slash'}),
#         help_text='Please enter the same password as above.',
#     )

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.password1.class_attribute = 'fa-eye-slash'
#     #     self.password2.class_attribute = 'fa-eye-slash'

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'birth_date', 'username', 'email', 'password1' ,'password2')

#     # widget=forms.TextInput(attrs={'class':'fa-eye-slash'}),

# class PasswordInputWithClass(forms.PasswordInput):
#     def __init__(self, attrs=None, render_value=False):
#         attrs = attrs or {}
#         attrs['class'] = 'password-input'
#         super().__init__(attrs, render_value)

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    # password1 = forms.CharField(widget=PasswordInputWithClass)
    # password2 = forms.CharField(widget=PasswordInputWithClass)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'username', 'email', 'password1', 'password2')

