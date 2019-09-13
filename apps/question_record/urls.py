__author__ = 'yuchen'
__date__ = '2018/11/23 13:32'

from django.conf.urls import url,include
from question_record import views


urlpatterns = [
    url(r"^index/$",views.show_index,name="show_my_questions"),
    url(r"^create/$",views.create_question,name="create_question"),
    url(r'^edit-(\d+)/$', views.edit_question,name="edit_question"),

    url(r"^kill-list$",views.question_kill_list,name="kill_question"),
    url(r"^kill-(\d+)$",views.question_kill)
]