#coding:utf-8
from django.conf.urls import url
from . import views
app_name ='app1'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^index/$',views.index,name='index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    url(r'^list/$',views.ulist,name = 'ulist'),
]