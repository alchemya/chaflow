from django.db import models

# Create your models here.


from django.db import models
from  users.models import UserProfile
from shortuuidfield import ShortUUIDField
# Create your models here.



class FlowTemplate(models.Model):
    """流程模版，具备扩展性"""
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)
    flow_type_choices = (('Alter', '变更流程'),)
    flow_type = models.CharField(choices=flow_type_choices, max_length=64)

    def __str__(self):
        return self.name


class Alter_Desc(models.Model):
    alter = models.ForeignKey("Alter",default=None)
    alter_momo =models.CharField("变更内容概括",max_length=255)

    change_type = models.SmallIntegerField(choices=((0, "功能优化"), (1, "问题修复"), (2, "数据调整"),(3,'测试环境调整'),(4,'数据导入导出')), verbose_name="修改类型")
    approve_user = models.CharField(max_length=128, verbose_name="提出人")
    alter_description = models.TextField("详细说明", blank=True, null=True)
    other_env = models.CharField(max_length=256,verbose_name="涉及环境")

    def __str__(self):
        return self.alter_momo



class Alter(models.Model):
    """流程总表，存储所有流程都会有的公共信息"""
    alter_id = ShortUUIDField(primary_key=True)
    template = models.ForeignKey(FlowTemplate,default=0)
    alter_title=models.CharField(max_length=255,verbose_name="变更名称")
    proposer = models.ForeignKey(UserProfile,verbose_name="变更申请人",default=None,related_name="proposer_alters")
    operator = models.ForeignKey(UserProfile,verbose_name="变更操作人",default=None,related_name="operator_alters")
    # content = models.TextField(blank=True,null=True,verbose_name="申请内容")
    in_queue = models.BooleanField(default=True,help_text="只要任务没被人处理，就会一直在queue中")
    start_time = models.DateTimeField("开始时间")
    end_time = models.DateTimeField("结束时间")
    date = models.DateTimeField(auto_created=True,auto_now=True,verbose_name="创建时间")
    risk_level = models.SmallIntegerField(choices=((0,"低"), (1,"中"), (2,"高")),verbose_name="风险等级")
    alter_type_choice = ((0, "一般变更"), (1, "紧急变更"),(2,"特急变更"))
    alter_type = models.SmallIntegerField(choices=alter_type_choice,verbose_name="变更类型",default=None)
    memo = models.TextField('备注', blank=True, null=True, default=None)

    alter_effect = models.SmallIntegerField(choices=((0, "无影响"), (1, "业务中断")), verbose_name="业务影响",default=0)
    alter_stop_time = models.CharField(max_length=128,verbose_name="业务中断时间",default=None)
    alter_stop_range = models.CharField(max_length=128,verbose_name="业务中断范围",default=None)
    technical_director = models.ForeignKey(UserProfile, verbose_name="团队技术负责人", related_name="technical_director_alters",default=None)
    customer_director = models.ForeignKey(UserProfile, verbose_name="团队技术负责人",related_name="customer_director_alters",default=None)

    technical_director_opnion = models.TextField(max_length=500,verbose_name="团队技术负责人意见",default=None)
    committee_opnion = models.TextField(max_length=500,verbose_name="方案评审会评审意见",default=None)

    implement_plan = models.TextField(max_length=500, verbose_name="实施方案", default=None)
    implement_plan_time = models.CharField(max_length=128, verbose_name="实施方案预期耗时", default=None)
    implement_validate_plan = models.TextField(max_length=500, verbose_name="实施后验证方案", default=None)
    implement_validate_plan_time = models.CharField(max_length=128, verbose_name="实施后验证方案预期耗时", default=None)

    back_plan =  models.TextField(max_length=500,verbose_name="回退方案",default=None)
    back_plan_time = models.CharField(max_length=128, verbose_name="回退方案预期耗时",default=None)
    back_validate_plan = models.TextField(max_length=500, verbose_name="应急处理后验证方案",default=None)
    back_validate_plan_time = models.CharField(max_length=128, verbose_name="处理后预期耗时",default=None)

    yingji_plan = models.TextField(max_length=500, verbose_name="应急预案", default=None)
    yingji_plan_time = models.CharField(max_length=128, verbose_name="应急预案预期耗时", default=None)
    yingji_validate_plan = models.TextField(max_length=500, verbose_name="回退后验证方案", default=None)
    yingji_validate_plan_time = models.CharField(max_length=128, verbose_name="回退后验证方案预期耗时", default=None)
    alter_status_choice = ((0,"已提交"),(1,"保存未提交"),(2,"被打回"),(3,"流程完成"))
    alter_status = models.SmallIntegerField(choices=alter_status_choice,verbose_name="变更状态",default=0)



    def __str__(self):
        return "变更名称:%s 发起人:%s" %(self.alter_title,self.proposer)





class Step(models.Model):
    """流程的每个环节"""
    flow_template = models.ForeignKey("FlowTemplate", verbose_name="所属流程")
    name = models.CharField("环节名称",max_length=128)
    description = models.TextField("环节介绍",blank=True,null=True)
    #order 的目的是用来用int格式来记录所处的流程状态，我的设计思路是，可以有n个order，只要你想。通过order的大小数值来记录顺序
    order = models.PositiveSmallIntegerField("环节步骤")
    role = models.ForeignKey("FlowRole",verbose_name="审批角色")
    is_countersign =  models.BooleanField("会签环节",default=False)
    required_polls = models.PositiveSmallIntegerField("会签最少需同意的人数",blank=True,null=True)


    def __str__(self):
        return "环节:%s 状态:%s" %(self.name,self.order)

    class Meta:
        unique_together = ("flow_template",'order')


class FlowRecord(models.Model):
    """流程的流转记录"""
    flow = models.ForeignKey("Alter",default=None)
    step = models.ForeignKey("Step")
    step_status_choice = ((0, "环节未开始"), (1, "环节已结束"))
    step_status = models.SmallIntegerField(choices=step_status_choice, verbose_name="当前环节状态", default=0)
    user = models.ForeignKey(UserProfile,verbose_name="审批用户",blank=True,null=True)
    status_choices = ((0,'同意'),(1,'拒绝'),(2,'需额外审批人审批'),(3,'待处理'))
    status = models.SmallIntegerField(choices=status_choices,verbose_name="审批状态")
    comment = models.TextField(max_length=1024, verbose_name="审批意见",default=None,null=True,blank=True)
    extra_parties = models.ManyToManyField(UserProfile,verbose_name="额外审批人列表",
                                           related_name="related_parties",
                                           blank=True)
    date = models.DateTimeField("添加时间",auto_now=True)


    def __str__(self):
        return "%s:%s" %(self.step,self.get_status_display())


class FlowRole(models.Model):
    """流程角色"""
    name = models.CharField(max_length=64,unique=True)
    users = models.ManyToManyField(UserProfile,blank=True)
    is_dynamic_role = models.BooleanField(default=False)
    role_lookup_func = models.CharField("查找动态role的函数",max_length=64,blank=True,null=True)

    def __str__(self):
        return self.name

