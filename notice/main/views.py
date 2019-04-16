from django.shortcuts import render
from .models import question,answer
from .forms import questionForm,answerForm
from django.contrib.auth.mixins	import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class index_forum(ListView):
	model = question
	template_name = 'main/index.html'
	context_object_name = 'datas'
	ordering = ['-date_q']

class forum_detail(DetailView):
	model = question
	template_name= 'main/detailpost.html'
	ordering = ['-date_q']

class PostCreate(LoginRequiredMixin,CreateView):
	model = question
	fields= ['title_q','notice_q','date_q','url_q']
	context_object_name = 'form'
	template_name = 'main/forum_write.html' 
	def form_valid(self,questionForm):
		questionForm.instance.author_q = self.request.user
		return super().form_valid(questionForm)

class ansCreate(LoginRequiredMixin,CreateView):
	model  = answer
	fields = ['notice_a','date_a','url_a','ques']
	context_object_name = 'form'
	template_name = 'main/ans_write.html' 
	def form_valid(self,answerForm):
		answerForm.instance.author_a = self.request.user
		return super().form_valid(answerForm)

def answer_detail(request,pk):
	kquery = answer.objects.filter(ques = pk)
	context = {'kquery':kquery}
	return render(request,'main/detailanswer.html',context)
