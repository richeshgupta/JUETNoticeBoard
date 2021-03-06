from django.shortcuts import render,redirect
from .models import question,answer
from .forms import questionForm,answerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins	import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import reportques,reportans
from django.contrib.auth.models import User

class index_forum(ListView): 
	model = question
	template_name = 'main/index.html'
	context_object_name = 'datas'
	ordering = ['-date_q']

class forum_detail(DetailView):
	model = question
	template_name= 'main/detailpost.html'
	ordering = ['-date_q']

class answer_independent(DetailView):
	model = answer
	template_name = 'main/ans.html'
	def get_context_object(self,**kwargs):
		self.answer.views+=1;
		self.answer.save()
		return super().get_context_object(**kwargs)

class PostCreate(LoginRequiredMixin,CreateView):
	model = question
	fields= ['title_q','notice_q','date_q','url_q','tag1_q','tag2_q',]
	context_object_name = 'form'
	template_name = 'main/forum_write.html'
	def form_valid(self,questionForm):
		questionForm.instance.author_q = self.request.user
		return super().form_valid(questionForm)
	
class ansCreate(LoginRequiredMixin,CreateView):
	model  = answer
	fields = ['title_a','notice_a','ques','date_a','url_a','tag1_a','tag2_a',]
	context_object_name = 'form'
	template_name = 'main/ans_write.html'
	def form_valid(self,answerForm):
		answerForm.instance.author_a = self.request.user
		return super().form_valid(answerForm)

def answer_detail(request,pk):
	kquery = answer.objects.filter(ques = pk).order_by('-upvotes')
	context = {'kquery':kquery}
	return render(request,'main/detailanswer.html',context)

class question_delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = question
	success_url = '/forum/'
	def test_func(self):
		test_case = self.get_object()
		if self.request.user == test_case.author_q:
			return True
		else:
			return False

class AnswerDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model  = answer
	success_url = '/forum/'
	def test_func(self):
		test_case = self.get_object()
		if self.request.user == test_case.author_a:
			return True
		else:
			return False

class QuestionUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = question
	fields= ['title_q','notice_q','ques','date_q','url_q','tag1_q','tag2_q',]
	context_object_name = 'form'
	def form_valid(self,questionForm):
		questionForm.instance.author_q = self.request.user
		return super().form_valid(questionForm)
	def test_func(self):
		test_case = self.get_object()
		if self.request.user == test_case.author_q:
			return True
		else:
			return False

class AnswerUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = answer
	fields = ['notice_a','date_a','url_a','tag1_a','tag2_a',]
	context_object_name = 'form'
	def form_valid(self,answerForm):
		answerForm.instance.author_a = self.request.user
		return super().form_valid(answerForm)
	def test_func(self):
		test_case = self.get_object()
		if self.request.user == test_case.author_a:
			return True
		else:
			return False

@login_required
def upvotes(request,pk):
	query = answer.objects.get(id = pk)
	query.upvotes+=1;
	query.save();
	return render(request,"main/upvoted.html",{})
@login_required
def downvotes(request,pk):
	query = answer.objects.get(id = pk)
	query.upvotes-=1;
	query.save();
	return render(request,"main/downvoted.html",{})

@login_required
def reportq(request,pk):
	query = question.objects.get(id = pk)
	try:
		kquery = reportques.objects.get(reported_q=query,reported_by = request.user)
	except:
		kquery = reportques(reported_q = query,reported_by = request.user)
	kquery.save();
	return render(request,"main/reported.html",{})

@login_required
def reporta(request,pk):
	query = answer.objects.get(id = pk)
	try:
		kquery = reportans.objects.get(reported_a=query)
	except:
		kquery = reportans(reported_a = query)
	kquery.save();
	return render(request,"main/reported.html",{})

def profile(request,pk):
	qquery = question.objects.filter(author_q = pk)
	author = User.objects.get(id = pk)
	context= {'qquery':qquery,'author':author}
	return render(request,"main/profile.html",context)

def donate(request):
	return render(request,"main/donate.html",{})

def faqs(request):
	return render(request,"main/faqs.html",{})

def guidelines(request):
	return render(request,"main/guidelines.html",{})