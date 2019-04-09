from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index_mail(request):
	send_mail('Notice Board',
			'New Post has been Added',
			'pantomath.notice@gmail.com',
			['satyamupadhyay260@gmail.com','rgrichesh45@gmail.com'],
			fail_silently = False)
	return render(request, 'send/index.html',{})
