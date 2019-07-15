from django import forms
from django.contrib.auth.models import User
from .models import question,answer
#from django.utils.translation import ugettext_lazy as _
class questionForm(forms.ModelForm):
	
	class Meta: 
		model = question
		fields= ['title_q','notice_q','date_q','url_q','tag1_q','tag2_q',]


class answerForm(forms.ModelForm):
	
	class Meta: 
		model = answer
		fields= ['title_a','notice_a','date_a','url_a','ques','tag1_a','tag2_a',]
