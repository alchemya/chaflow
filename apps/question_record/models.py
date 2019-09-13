from django.db import models
from users.models import UserProfile

# Create your models here.

class QuestionRecord(models.Model):
    create_date = models.DateField("发生日期",blank=True,auto_now_add=True)
    create_time = models.TimeField("发生时间",blank=True,auto_now_add=True)
    action_time = models.TimeField("响应时间",blank=True,auto_now=True)
    position_time=models.TimeField("定位时间",blank=True,auto_now=True)
    question_result=models.CharField('问题进展', blank=True, null=True, default=None,max_length=125)
    question_memo = models.TextField('问题简述', blank=True, null=True, default=None)
    question_reason=models.CharField('问题原因',blank=True,null=True,default=None,max_length=100)
    question_range=models.CharField('问题影响范围',blank=True,null=True,default=None,max_length=50)
    class Meta:
        verbose_name = '问题记录'
        verbose_name_plural = verbose_name

class Ask_Question(models.Model):
    title = models.CharField(max_length=32)
    detail = models.TextField()
    user = models.ForeignKey(UserProfile,related_name='u')
    # ctime = models.CharField(max_length=32) # 1491527007.452494
    ctime = models.DateTimeField("提交时间",auto_now_add=True)
    status_choices = (
        (1,'未处理'),
        (2,'处理中'),
        (3,'已处理'),
    )
    status = models.IntegerField(choices=status_choices,default=1)

    processer = models.ForeignKey(UserProfile,related_name='p',null=True,blank=True)
    solution = models.TextField(null=True)
    ptime = models.DateTimeField(null=True)
    pj_choices = (
        (1, '不满意'),
        (2, '一般'),
        (3, '工作很赞'),
    )
    pingjia = models.IntegerField(choices=pj_choices,null=True,default=2)