from dataclasses import field
from django import forms
from .models import todoList
from Accounts.models import Users
from PIL import Image

class todoForm(forms.ModelForm):
    class Meta:
        model=todoList
        fields = ['task','action','picture']
class customForm(forms.ModelForm):
    class Meta:
        model=Users
        fields = ['first_name','last_name','profile_picture']
    # def clean(self):
    #     super(customForm, self).clean()
    #     profile_picture = self.cleaned_data.get('profile_picture')
    #     check_Image = Image.open(profile_picture)
    #     print(check_Image.verify())
    #     if check_Image.verify():
    #         print("ADASdasd")
    #     return self.cleaned_data
        