from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PasswordManager(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    appname = models.CharField(max_length=500)
    applink=models.CharField(max_length=1000)
    email=models.EmailField(max_length=500)
    password = models.CharField(max_length=500)
    def __str__(self):
       return self.appname
    
class FormTest(models.Model):
    postname = models.CharField(max_length=2500)
    postbody = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.postname