from django import forms
from django.contrib.auth.models import User
from .models import question,answer

class questionForm(forms.ModelForm):
	
	class Meta: 
		model = question
		fields= ['title_q','notice_q','date_q','url_q']

class answerForm(forms.ModelForm):
	
	class Meta: 
		model = answer
		fields= ['notice_a','date_a','url_a','ques']
