__author__ = 'yuchen'
__date__ = '2018/11/29 00:14'

from django import forms
from django.forms import widgets

class QuestionMaker(forms.Form):
    title = forms.CharField(max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control '}))
    detail = forms.CharField(widget=widgets.Textarea(attrs={'id':'detail','class':'kind-content'}))

class QuestionKill(forms.Form):
    title = forms.CharField(max_length=128,required=False,widget=widgets.TextInput(attrs={'class': 'form-control',"disabled":"disabled"}))
    detail = forms.CharField(widget=widgets.Textarea(attrs={'id': 'detail', 'class': 'kind-content'}))
    solution = forms.CharField(widget=widgets.Textarea(attrs={'id':'solution','class':'kind-content'}))