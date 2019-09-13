__author__ = 'yuchen'
__date__ = '2018/12/4 00:55'

from . import permission_hook


perm_dic = {

    'crm_table_index': ['table_index', 'GET', [], {}, permission_hook.view_my_own_customers ],  # 可以查看APP里所有数据库表
    'crm_table_list': ['table_list', 'GET', [], {},permission_hook.view_my_own_customers],  # 可以查看每张表里所有的数据
    'crm_table_list_view': ['table_change', 'GET', [], {}],  # 可以访问表里每条数据的修改页
    'crm_table_list_change': ['table_change', 'POST', [], {}],
    'crm_table_obj_add': ['login', 'GET', [], {}],

}