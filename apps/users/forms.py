__author__ = 'yuchen'
__date__ = '2019/2/14 11:34'


from django import forms
from django.forms import widgets

#编辑用户信息的表单
class EditUserForm(forms.Form):
    postion = forms.CharField(required=False,label="工作职位",widget=widgets.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=False,label="邮箱",widget=widgets.EmailInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(required=False,label="电话",widget=widgets.TextInput(attrs={'class':'form-control'}))
    company = forms.CharField(required=False,label="公司",widget=widgets.TextInput(attrs={'class':'form-control'}))
    department = forms.CharField(required=False,label="所属团队",widget=widgets.TextInput(attrs={'class':'form-control'}))
    memo = forms.CharField(required=False,label="个人简介",widget=widgets.Textarea(attrs={'class': 'form-control',"rows":"3"}))

#重置密码的表单
class ChangePwdForm(forms.Form):
    '''重置密码'''
    old_password = forms.CharField(required=True,min_length=5,max_length=99)
    password1 = forms.CharField(required=True, min_length=5,max_length=99)
    password2 = forms.CharField(required=True, min_length=5,max_length=99)