from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import Users,Code
from django.contrib.auth.models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=Users
    list_display=('email','is_staff','is_active')
    list_filter=('email','is_staff','is_active')
    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Permissions',{'fields':('is_staff','is_active')})
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_staff','is_active')
        }),
    )
    search_fields=('email',)
    ordering=('email',)

admin.site.register(Users,CustomUserAdmin)
admin.site.register(Code)