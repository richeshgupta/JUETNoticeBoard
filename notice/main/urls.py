from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostCreate,forum_detail,ansCreate,answer_detail,question_delete,QuestionUpdate
from .views import upvotes,downvotes,AnswerUpdate,AnswerDelete
from .views import reportq,reporta,profile,donate
urlpatterns= [
	path('', views.index_forum.as_view(),name="forum-home"),
	path('write/',PostCreate.as_view(template_name='main/forum_write.html'),name='write'),
    path('question/<int:pk>/',forum_detail.as_view(),name="forum_detail"),
    path('answer/<int:pk>/',ansCreate.as_view(),name="create-ans"),
    path('show-answer/<int:pk>/',answer_detail,name="ans-detail"),
    path('del-ques/<int:pk>/',question_delete.as_view(),name='delete-ques'),
    path('update-ques/<int:pk>/',QuestionUpdate.as_view(),name='update-ques'),
    path('upvote/<int:pk>/',upvotes,name='upvote'),
    path('downvote/<int:pk>/',downvotes,name='downvote'),
    path('update_ans/<int:pk>/',AnswerUpdate.as_view(),name='update-ans'),
    path('delete_ans/<int:pk>/',AnswerDelete.as_view(),name='delete-ans'),
    path('reportq/<int:pk>/',reportq,name='report-q'),
    path('reporta/<int:pk>/',reporta,name='report-a'),
    path('profile/<int:pk>/',profile,name='profile'),
    path('donate/',donate,name='donate'),

]