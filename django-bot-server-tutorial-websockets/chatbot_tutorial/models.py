from django.db import models
from django.contrib.auth.models import User
import datetime
import os

class User(models.Model):
    User_name=models.CharField(max_length=150,null=False,blank=False)
    Number_of_calls=models.IntegerField(null=False,blank=False)
    time=models.DateTimeField(max_length=5000,null=False,blank=False)
    


    def __str__(self):
        return self.User_name

 