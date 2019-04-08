from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
# Create your models here.
class NoticeBoard(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100,unique = True)
	notice = models.TextField(max_length=1000,default='',unique = True)
	date = models.DateTimeField(default = timezone.now)
	url = models.URLField(max_length=100,blank = True)

	def __str__(self):
		return self.title
	