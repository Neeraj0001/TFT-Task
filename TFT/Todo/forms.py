from dataclasses import field
from django import forms
from .models import todoList
class todoForm(forms.ModelForm):
    class Meta:
        model=todoList
        fields = ['task','action']