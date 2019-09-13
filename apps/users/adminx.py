__author__ = 'yuchen'
__date__ = '2018/11/21 13:54'

import xadmin
from .models import Role,Menus

from xadmin import views#引入xadmin的主题页面视图函数

#主题定制修改
class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlogbalSettings(object):
    site_title='CHA后台管理系统'
    site_footer='Cha'
    menu_style='accordion'
#
class RoleAdmin(object):
    list_display=["name"]
    search_field=["name"]
    list_filter=["name"]


xadmin.site.register(views.BaseAdminView,BaseSetting)#注册主题
xadmin.site.register(views.CommAdminView,GlogbalSettings)
xadmin.site.register(Role)
xadmin.site.register(Menus)





