from django.db import models
from Accounts.models import Users
# Create your models here.
class todoList(models.Model):
    task = models.CharField(max_length=200)
    action = models.BooleanField(default=False)
    user= models.ForeignKey(Users,on_delete=models.CASCADE)
    def __str__(self):
        return self.task +'|'+str(self.user.first_name) 