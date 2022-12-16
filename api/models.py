from django.db import models
from django.contrib.auth.models import User
from .helpers import *
# Create your models here.
class VideoComment(models.Model):
    comment = models.TextField(default=None,null=True,blank=True)
    user = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE,null=True,blank=True,default=None)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,default=None)
    parent_name = models.CharField(max_length=225,null=True,blank=True,default=None)
    parent_comment = models.TextField(null=True,blank=True,default=None)
    datestamp = models.CharField(max_length=225,default=None,null=True,blank=True)
    timestamp = models.CharField(max_length=225,default=None,null=True,blank=True)



class ContactUs(models.Model):
    name = models.CharField(max_length=225,null=True,blank=True,default=None)
    email = models.EmailField(default=None,blank=True,null=True)
    message = models.TextField(default=None,blank=True,null=True)