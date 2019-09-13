__author__ = 'yuchen'
__date__ = '2018/11/28 12:32'

#_*_coding:utf-8_*_
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request,"question_record/index.html")

@login_required
def page_not_found(request):
    return render(request,'common/404.html',status=404)

@login_required
def page_error(request):
    return render(request, 'common/500.html',status=500)

@login_required
def permission_denied(request):
    return render(request, 'common/403.html',status=403)
