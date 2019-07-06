from django import forms
from django.contrib.auth.models import User
from .models import NoticeBoard
from django.contrib.auth.forms import UserCreationForm

class Notice_board_class(forms.ModelForm):
	class Meta:
		model = NoticeBoard
		fields = ['title','notice','date','url','docs']
class kk(UserCreationForm):
	email = forms.EmailField(max_length=60)
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2']
