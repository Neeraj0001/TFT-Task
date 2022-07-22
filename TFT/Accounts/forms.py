from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=Users
        fields=('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=Users
        fields=('email',)
    