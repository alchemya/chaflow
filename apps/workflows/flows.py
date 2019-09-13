__author__ = 'yuchen'
__date__ = '2019/2/6 11:03'


from workflows import models

class FlowManger(object):
    """负责flow分配"""
    def __init__(self,request):
        self.request = request

    def get_assigned_to_me_flowlist(self):
        """
        思路：根据自己的角色找到所有与我有关的steps，再根据这些step id到flow_record表里找出正处于当前这些step且还没有被处理的记录
        """

        related_steps = []
        for role in self.request.user.flowrole_set.all():
            print("related role", role, role.step_set.all() )
            related_steps.extend(role.step_set.all() )
        print(related_steps)

        related_flow_record_objs = models.FlowRecord.objects.filter(step__in=related_steps,status=3).order_by('-date')
        print("related_flow_record_objs",related_flow_record_objs)
        return related_flow_record_objs
