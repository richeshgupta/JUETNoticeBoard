from django import forms
from django.contrib.auth.models import User
from .models import NoticeBoard

class Notice_board_class(forms.ModelForm):
	
	class Meta: 
		model = NoticeBoard
		fields= ['title','notice','date','url','docs']

