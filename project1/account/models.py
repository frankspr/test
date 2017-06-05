#coding:utf-8
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    regist_time = models.DateTimeField(auto_now_add=True,)
    latest_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username

class aaa(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    regist_time = models.DateTimeField(auto_now_add=True,)
    latest_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username


