from dataclasses import field
from django import forms
from .models import todoList
from Accounts.models import Users

class todoForm(forms.ModelForm):
    class Meta:
        model=todoList
        fields = ['task','action','picture']
class customForm(forms.ModelForm):
    class Meta:
        model=Users
        fields = ['first_name','last_name','profile_picture']