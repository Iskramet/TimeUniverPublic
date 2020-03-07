from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Group as groupdb

class GroupForm(forms.Form):
    group = forms.ModelChoiceField(queryset=groupdb.objects.all(), empty_label=None) 

