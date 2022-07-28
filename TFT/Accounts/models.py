import code
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import random
import os
from datetime import datetime   

# Create your models here.
def image_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s-%s.%s" % (instance.first_name, instance.last_name,instance.id, ext)
    return os.path.join('profile_picture', filename)
class Users(AbstractUser):
    username=None
    email=models.EmailField(_('email address'),unique=True)
    profile_picture = models.ImageField(upload_to=image_file_name,null=True, blank=True,default="user_logo.png")
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
    def __str__(self):
        return self.email

class Code(models.Model):
    user=models.OneToOneField(Users,on_delete=models.CASCADE)
    otp=models.CharField(max_length=5,blank=True)
    date_time= models.DateTimeField(default=datetime.now, blank=True)
    def save(self,*args,**kwargs):
        number_list=[x for x in range(10)]
        code_items=[]
        for i in range(5):
            num=random.choice(number_list)
            code_items.append(num)
        code_string="".join(str(items) for items in code_items)
        self.otp=code_string
        self.date_time=datetime.now()
        super().save(*args,**kwargs)