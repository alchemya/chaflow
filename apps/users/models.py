# Create your models here.

from datetime import datetime
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,Group,PermissionsMixin
)
import django
from django.contrib.auth.models import AbstractUser



class Role(models.Model):
    '''角色表'''
    name = models.CharField(max_length=64,unique=True)
    #一个角色可以访问多个菜单，一个菜单可以被多个角色访问
    menus = models.ManyToManyField('Menus',blank=True,verbose_name='动态菜单')

    def __str__(self):
        return self.name


class Menus(models.Model):
    '''动态菜单'''
    name = models.CharField(max_length=64)
    # 绝对url和动态url
    url_type_choices = ((0, 'absolute'), (1, 'dynamic'))
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0)
    url_name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    class Meta:
        unique_together = ('name', 'url_name')
    class Meta:
        verbose_name = '角色网址'
        verbose_name_plural = verbose_name


class UserProfile(AbstractUser):
    postion = models.CharField(max_length=100,verbose_name='职位',blank=True,null=True,default="")
    company=models.CharField(max_length=100,verbose_name="公司",blank=True,null=True,default="")
    department=models.CharField(max_length=50,verbose_name="所属团队",blank=True,null=True,default="")
    mobile=models.CharField(max_length=11,null=False,blank=True,verbose_name="联系电话",default="")
    memo = models.TextField('备注', blank=True, null=True, default=None)
    valid_begin_time = models.DateTimeField("使用权限开始日期",default=django.utils.timezone.now)
    valid_end_time = models.DateTimeField("使用权限结束日期(可以不设置)",blank=True, null=True)
    photo = models.ImageField('个人头像',blank=True,help_text="为了节省存储资源，图片采取了字节流的方式保存在数据库中,在这里上传无法生效")
    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name
        permissions = (
            ('crm_table_list', '可以查看每张表里所有的数据'),
            ('crm_table_list_view', '可以访问表里每条数据的修改页'),
            ('crm_table_list_change', '可以对表里的每条数据进行修改'),
            ('crm_table_obj_add_view', '可以访问每张表的数据增加页'),
            ('crm_table_obj_add', '可以对每张表进行数据添加'),
        )
    def __str__(self):
        return self.username

    # class Meta:
    #     permissions = (
    #         ('crm_table_list', '可以查看每张表里所有的数据'),
    #         ('crm_table_list_view', '可以访问表里每条数据的修改页'),
    #         ('crm_table_list_change', '可以对表里的每条数据进行修改'),
    #         ('crm_table_obj_add_view', '可以访问每张表的数据增加页'),
    #         ('crm_table_obj_add', '可以对每张表进行数据添加'),
    #
    #     )







