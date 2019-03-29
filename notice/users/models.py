from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
# Create your models here.
class NoticeBoard(models.Model):
	title = models.CharField(max_length=100)
	notice = models.TextField(max_length=1000,default='')
	date = models.DateTimeField(default = timezone.now)
	url = models.URLField(max_length=100,blank = True)