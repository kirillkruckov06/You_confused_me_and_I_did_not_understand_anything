from django.contrib.sitemaps.views import index
from django.template.defaultfilters import default
from django.urls import path, include
from .views import *
from django.contrib import admin

urlpatterns = [
    path('authorlist', AuthorList.as_view(template_name='index.html')),
    path('post/<int:pk>/', Post.as_view()),
    path('/postcreate/', PostCreate.as_view()),
    path('news_list/', index, name='index'),
    path('news/<str:slug>', default, name='default')
]