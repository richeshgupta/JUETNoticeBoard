from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class question(models.Model):
	author_q = models.ForeignKey(User, on_delete=models.CASCADE)
	title_q = models.CharField(max_length=100,unique = True)
	notice_q = models.TextField(max_length=1000,default='',unique = True)
	date_q = models.DateTimeField(default = timezone.now)
	url_q = models.URLField(max_length=100,blank = True)
	def __str__(self):
		return self.title_q
	
	def get_absolute_url(self):
		return reverse('forum-home')


class answer(models.Model):
	
	author_a = models.ForeignKey(User, on_delete=models.CASCADE)
	notice_a = models.TextField(max_length=1000,default='',unique = True)
	date_a = models.DateTimeField(default = timezone.now)
	url_a = models.URLField(max_length=100,blank = True)
	ques = models.ForeignKey(question,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.notice_a
	
	def get_absolute_url(self):
		return reverse('forum-home')

