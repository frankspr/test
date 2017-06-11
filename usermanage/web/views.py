#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse

def Index(request):
    return HttpResponse('<h1>Web.Index</h1>')