"""notice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from users.views import menu,not_logged_in,index_list,notice_detail,PostCreate,PostUpdate,notice_delete
from users.views import about
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',menu,name='menu'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('notice/',PostCreate.as_view(),name='notice'),
    path('home/',index_list.as_view(),name='home'),
    path('not_logged_in/',not_logged_in,name='not_logged_in'),
    path('route/<int:pk>/',notice_detail.as_view(),name="notice_detail"),
    path('route/<int:pk>/update/',PostUpdate.as_view(),name="notice_update"),
    path('route/<int:pk>/delete/',notice_delete.as_view(),name="notice_delete"),
    path('/send/',include('send.urls')),
    path('about/',about,name='about'),
    path('forum/',include('main.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)