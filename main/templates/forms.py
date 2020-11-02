from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    user_email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    name_of_company = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email_of_company = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    activation_code = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'user_email', 'password1', 'password2', 'name_of_company',
                  'email_of_company',
                  'activation_code')
