__author__ = 'yuchen'
__date__ = '2019/1/31 11:03'


from django.conf.urls import url,include

from workflows import views


urlpatterns = [


    #提交审批申请的页面
    url(r'^add_alters/$',views.add_alters,name="add_alters"),
    #只保存审批申请的页面
    url(r'save_alters/$',views.save_alters,name="save_alters"),
    #查看已提交的变更详情
    url(r"^show_alter/(\w+)/$",views.show_alter,name="show_alter"),
    #对于被打回的或处于保存状态的变更文档进行编辑操作
    url(r'^edit_alter/(\w+)/$',views.edit_alter,name="edit_alter"),
    #对于被打回的或处于保存状态的变更文档进行删除
    url(r'delete_alter/(\w+)/$',views.delete_my_submit_alter,name='delete_my_submit_alter'),
    #对于被打回的或处于保存状态的变更文档进行内容更新并提交工作流
    url(r'update_and_submit/(\w+)/$',views.update_and_submit,name='update_and_submit'),
    #对于被打回的或处于保存状态的变更文档只进行内容更新
    url(r'update_and_save/(\w+)/$',views.update_and_save,name='update_and_save'),
    # 我提交的变更申请的列表
    url(r'^show_my_alters/$', views.show_my_submit_alter,name='show_my_alters'),
    # 具体变更的流程环节详情
    url(r'^alter_detail/(\w+)/$', views.alter_detail, name='alter_detail'),
    # 需要我审批的流程
    url(r'^my_alter_approvals/$',views.my_alter_approvals,name="my_alter_approvals"),
    #具体审批页
    url(r'^alter_approve/(\w+)/$',views.alter_approve,name='alter_approve'),
    #我的审批记录  有小bug，暂时未改
    url(r'^my_approval_records/$', views.my_approval_records,name='my_approval_records'),
    # 提交的变更的实时流程态
    url(r'^alter_flow_real_time/(\w+)/$',views.alter_flow_real_time,name="alter_flow_real_time")






]
