__author__ = 'yuchen'
__date__ = '2019/1/31 11:04'



import xadmin
from .models import Alter_Desc,Alter,Step,FlowRole,FlowTemplate,FlowRecord



xadmin.site.register(Alter)
xadmin.site.register(Alter_Desc)
xadmin.site.register(Step)
xadmin.site.register(FlowTemplate)
xadmin.site.register(FlowRecord)
xadmin.site.register(FlowRole)