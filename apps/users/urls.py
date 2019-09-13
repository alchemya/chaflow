__author__ = 'yuchen'
__date__ = '2019/2/14 09:56'


from django.conf.urls import url,include
from users import views


urlpatterns = [
    url(r'^my_information/$',views.myself,name='my_information'),
    url(r'^edit_my_information/$',views.myself_edit,name='edit_my_information'),
    url(r'my_image/$',views.my_image,name='my_image'),
    url(r'user_info/(?P<user_id>\d+)/$',views.user_info,name='user_info')
    # url(r'^edit-my-information/$',views.myself_edit,name='edit_my_information'),
    # url(r'^my-image/$',views.my_image,name='my_image'),
]