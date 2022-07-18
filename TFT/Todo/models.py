from django.db import models

# Create your models here.
class todoList(models.Model):
    task = models.CharField(max_length=200)
    action = models.BooleanField(default=False)
    def __str__(self):
        return self.task +'|'+str(self.action) 