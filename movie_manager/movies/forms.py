from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import movies



class MovieForm(ModelForm):
    class Meta:
        model = movies
        fields = ['title', 'year', 'description']

from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
