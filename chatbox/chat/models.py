from django.db import models

from django.contrib.auth.models import AbstractUser





# Create your models here.
class Chat(models.Model):
    content=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True)
    group=models.ForeignKey('Group',on_delete=models.CASCADE)
    user=models.CharField(max_length=20,null=True)

    

class Group(models.Model):
    name=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return  self.name
    
    def getid(self):
        return self.id
    

    

    
   
   