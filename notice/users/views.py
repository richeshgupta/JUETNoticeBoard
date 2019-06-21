from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Notice_board_class as NoticeBoardForm
#from .forms import signup,UpdateUser
from .models import NoticeBoard
from django.contrib.auth.mixins	import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.mail import send_mail
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm



#Index page
class index_list(ListView):
	model = NoticeBoard
	template_name = 'users/index.html'
	context_object_name = 'data'
	ordering = ['-date']

#detail notice page
class notice_detail(DetailView):
	model = NoticeBoard

class PostCreate(LoginRequiredMixin,CreateView):
	model = NoticeBoard
	fields= ['title','notice','date','url','docs']
	context_object_name = 'form'
	def form_valid(self,NoticeBoardForm):
		NoticeBoardForm.instance.author = self.request.user
		send_mail('JUET NoticeBoard','New Post is Up : - \n Title :' + NoticeBoardForm.instance.title + '\n Post :' + NoticeBoardForm.instance.notice, 'pantomath.notice@gmail.com',
	    ['rgrichesh45@gmail.com','satyamupadhyay260@gmail.com'], fail_silently=False)
		return super().form_valid(NoticeBoardForm)

#updating code
class PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = NoticeBoard
	fields= ['title','notice','date','url']
	context_object_name = 'form'
	def form_valid(self,NoticeBoardForm):
		NoticeBoardForm.instance.author = self.request.user
		return super().form_valid(NoticeBoardForm)
	def test_func(self):
		test_case = self.get_object()
		if self.request.user == test_case.author:
			return True
		else:
			return False

#deleting post
class notice_delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = NoticeBoard
	success_url = '/home/'
	def test_func(self):
		test_case = self.get_object()
		if self.request.user == test_case.author:
			return True
		else:
			return False

def not_logged_in(request):
	return render(request,'users/not_logged_in.html',{})

def menu(request):
	return render(request,'users/initial.html',{})
	
def about(request):
	return render(request,'users/about.html',{})

#User creation
'''def signup_view(request):
    if request.method == 'POST':
        form = signup(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = signup()
    return render(request, 'signup.html', {'form': form})'''

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request,'users/signup.html',{'form':form})