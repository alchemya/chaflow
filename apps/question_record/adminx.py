__author__ = 'yuchen'
__date__ = '2018/11/21 17:00'

import xadmin
from .models import QuestionRecord,Ask_Question

xadmin.site.register(QuestionRecord)
xadmin.site.register(Ask_Question)


