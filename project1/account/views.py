#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from  django.template import RequestContext
from django import forms
from models import User

class UserForm(forms.Form):
    username = forms.CharField(label='用户',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!')
    else:
        uf = UserForm()
    return render(req,'regist.html',
                              context={'uf':uf}
                              )

def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact=username,password__exact=password)
            if user:
                response = HttpResponseRedirect('/account/index/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/account/login/')
    else:
        uf = UserForm()
    return render(req,'login.html',context={'uf':uf})

def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username})

def logout(req):
    response = HttpResponse('logout!')
    response.delete_cookie('username')
    return response

def ulist(req):
    user_list = User.objects.all().order_by('id')
    return render(req, 'userlist.html', context={'user_list': user_list})
