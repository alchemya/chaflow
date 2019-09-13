"""Cha_Flow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import xadmin
from Cha_Flow import views
from users import views as user_view
from workflows import views as workflow_view

urlpatterns = [
    url(r'^brain/', xadmin.site.urls),
    url(r"^questions/",include("question_record.urls",namespace="question")),
    url(r'^workflow/',include("workflows.urls",namespace="workflow")),
    url(r'^user/',include('users.urls',namespace='users')),
    url(r"^$",views.index,name="dashboard"),
    url(r"^login",user_view.acc_login,name="login"),
    url(r"^logout",user_view.acc_logout,name="logout"),


    url(r'^403.html',views.permission_denied,name='code 403'),
    url(r'^500.html',views.page_error,name='code 500')
]

# 定义错误跳转页面
handler404 = views.page_not_found
handler403 = views.permission_denied
handler500 = views.page_error
