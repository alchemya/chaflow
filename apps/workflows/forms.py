__author__ = 'yuchen'
__date__ = '2019/1/31 11:03'

#_*_coding:utf-8_*_

from django import forms
from django.forms import widgets
from users import models

class ApprovalForm(forms.Form):
    comment = forms.CharField(label="你的审批意见",widget=forms.Textarea(attrs={'class': "form-control"}))
    status_choices = ((0, '同意'), (1, '拒绝'))
    status = forms.IntegerField(label="审批结果",widget=forms.widgets.Select(choices=status_choices,attrs={'class': "form-control"}))



class AlterMaker(forms.Form):
    alter_title = forms.CharField(label="变更标题",max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control'}))
    operator = forms.IntegerField(label="变更操作人",widget=widgets.Select(attrs={'class': 'form-control  select2' }))
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    risk_level=forms.IntegerField(label="风险等级",widget=forms.widgets.Select(choices=((0,"低"), (1,"中"), (2,"高")),attrs={'class': 'form-control'}))
    alter_type=forms.IntegerField(label="变更类型",widget=forms.widgets.Select(choices=((0, "普通变更"), (1, "紧急变更"),(2,"特急变更")),attrs={'class': 'form-control'}))
    memo = forms.CharField(label="备注",widget=widgets.TextInput(attrs={'class':'form-control','placeholder':'备注信息可以不填'}),required=False)

    alter_momo = forms.CharField(label="变更内容概括",widget=widgets.Textarea(attrs={'class': 'form-control',"rows":"3"}))
    change_type = forms.IntegerField(label="修改类型", widget=forms.widgets.Select(choices=((0, "功能优化"), (1, "问题修复"), (2, "数据调整"),(3,'测试环境调整'),(4,'数据导入导出')),attrs={'class': 'form-control select2'}))
    approve_user = forms.CharField(label="提出人",max_length=128, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    alter_description = forms.CharField(label="详细说明",widget=widgets.Textarea(attrs={'id': 'detail', 'class': 'kind-content'}))
    other_env = forms.CharField(label="涉及环境",max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control'}))

    alter_effect = forms.IntegerField(label="业务影响",widget=forms.widgets.Select(choices=((0, "无影响"), (1, "业务中断")),
                                                                attrs={'class': 'form-control'}))
    alter_stop_time = forms.CharField(label="业务中断时间", max_length=128,
                                  widget=widgets.TextInput(attrs={'class': 'form-control',"placeholder":"如果没有，请填写无"}))
    alter_stop_range = forms.CharField(label="业务中断范围", max_length=128,
                                      widget=widgets.TextInput(attrs={'class': 'form-control',"placeholder":"如果没有，请填写无"}))
    technical_director = forms.IntegerField(label="团队技术负责人", widget=widgets.Select(attrs={'class': 'form-control  select2'}))
    customer_director = forms.IntegerField(label="客户负责人", widget=widgets.Select(attrs={'class': 'form-control  select2'}))

    technical_director_opnion = forms.CharField(label="团队技术负责人意见",widget=widgets.Textarea(attrs={'class': 'form-control',"rows":"2"}))
    committee_opnion = forms.CharField(label="方案评审会评审意见",widget=widgets.Textarea(attrs={'class': 'form-control', "rows": "2"}))

    implement_plan = forms.CharField(label="实施方案", max_length=500, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    implement_plan_time = forms.CharField(label="实施方案预计耗时", max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control'}))
    implement_validate_plan = forms.CharField(label="实施后验证方案", max_length=500,widget=widgets.TextInput(attrs={'class': 'form-control'}))
    implement_validate_plan_time = forms.CharField(label="实施后预计耗时", max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control'}))

    back_plan = forms.CharField(label="回退方案",max_length=500,widget=widgets.TextInput(attrs={'class': 'form-control'}))
    back_plan_time = forms.CharField(label="回退方案预计耗时",max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control'}))
    back_validate_plan = forms.CharField(label="回退后验证方案", max_length=500, widget=widgets.TextInput(attrs={'class': 'form-control'}))
    back_validate_plan_time = forms.CharField(label="回退后预计耗时", max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control'}))

    yingji_plan = forms.CharField(label="应急预案",max_length=500,widget=widgets.TextInput(attrs={'class': 'form-control','placeholder':'应急预案可以不填'}),required=False)
    yingji_plan_time = forms.CharField(label="应急预案预期耗时",max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control','placeholder':'可以不填'}),required=False)
    yingji_validate_plan= forms.CharField(label="应急处理后验证方案", max_length=500, widget=widgets.TextInput(attrs={'class': 'form-control','placeholder':'应急处理后验证方案可以不填'}),required=False)
    yingji_validate_plan_time = forms.CharField(label="验证方案预期耗时", max_length=128,widget=widgets.TextInput(attrs={'class': 'form-control','placeholder':'可以不填'}),required=False)

    def __init__(self, *args, **kwargs):
        super(AlterMaker, self).__init__(*args, **kwargs)
        self.fields['operator'].widget.choices = models.UserProfile.objects.all().values_list('id','username')
        self.fields['technical_director'].widget.choices = models.UserProfile.objects.all().values_list('id', 'username')
        self.fields['customer_director'].widget.choices = models.UserProfile.objects.all().values_list('id', 'username')





