from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostCreate,forum_detail,ansCreate,answer_detail,question_delete,QuestionUpdate
urlpatterns= [
	path('', views.index_forum.as_view(),name="forum-home"),
	path('write/',PostCreate.as_view(template_name='main/forum_write.html'),name='write'),
	path('lgin/',auth_views.LoginView.as_view(template_name='main/login.html'),name='forum-login'),
    path('lgout/',auth_views.LogoutView.as_view(template_name='main/logout.html'),name='forum-logout'),
    path('route/<int:pk>/',forum_detail.as_view(),name="forum_detail"),
    path('answer/<int:pk>/',ansCreate.as_view(),name="create-ans"),
    path('show-answer/<int:pk>/',answer_detail,name="ans-detail"),
    path('del-ques/<int:pk>/',question_delete.as_view(),name='delete-ques'),
    path('update-ques/<int:pk>/',QuestionUpdate.as_view(),name='update-ques'),
]