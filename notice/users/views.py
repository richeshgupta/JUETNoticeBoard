from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Notice_board_class as NoticeBoardForm
from .models import NoticeBoard
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView

#Index page
class index_list(ListView):
	model = NoticeBoard
	template_name = 'users/index.html'
	context_object_name = 'data'
	ordering = ['-date']

#detail notice page
class notice_detail(DetailView):
	model = NoticeBoard


@login_required(login_url='not_logged_in')
def post(request):	
	form = NoticeBoardForm(request.POST)
	if form.is_valid():
		form.save()
		NoticeBoardForm()
	else:
		form = NoticeBoardForm()
	context = {'form':form}
	return render(request,'users/write.html',context)

def not_logged_in(request):
	return render(request,'users/not_logged_in.html',{})
def menu(request):
	return render(request,'users/initial.html',{})