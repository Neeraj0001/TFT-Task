import code
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import random

# Create your models here.
class Users(AbstractUser):
    username=None
    email=models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
    def __str__(self):
        return self.email

class Code(models.Model):
    user=models.OneToOneField(Users,on_delete=models.CASCADE)
    otp=models.CharField(max_length=5,blank=True)
    def save(self,*args,**kwargs):
        number_list=[x for x in range(10)]
        code_items=[]
        for i in range(5):
            num=random.choice(number_list)
            code_items.append(num)
        code_string="".join(str(items) for items in code_items)
        self.otp=code_string
        super().save(*args,**kwargs)