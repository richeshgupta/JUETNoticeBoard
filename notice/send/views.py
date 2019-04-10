from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.template.loader import get_template
# Create your views here.

def index_mail(request):
	subject 			= "New Post is up - JUET Notice Board"
	to_mail 			= ['rgrichesh45@gmail.com','satyamupadhyay260@gmail.com']
	from_acc 			= 'pantomath.notice@gmail.com'
	message 			= get_template('send/mail_temp.html').render()
	msg 				= EmailMessage(subject,message,to=to_mail,from_email=from_acc)
	msg.content_subtype	='html'
	msg.send()
	return render(request,'send/index.html',{})