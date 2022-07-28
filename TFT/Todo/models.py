from django.db import models
from Accounts.models import Users
import os
# Create your models here.
def image_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s-%s-task-%s.%s" % (instance.user.first_name, instance.user.last_name,filename, ext)
    return os.path.join('uploads', filename)
from django.db import models
from Accounts.models import Users
import os
class todoList(models.Model):
    task = models.CharField(max_length=200)
    action = models.BooleanField(default=False)
    picture = models.ImageField(upload_to=image_file_name,null=True, blank=True)
    description = models.CharField(max_length=200,blank=True,null=True)
    img_format_valid = models.BooleanField(default=False,blank=True,null=True)
    user= models.ForeignKey(Users,on_delete=models.CASCADE)
    def __str__(self):
        return self.task +'|'+str(self.user.first_name) +'|'+str(self.user.email)