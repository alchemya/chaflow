from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse
from .models import Alter,Alter_Desc,FlowRecord,Step
from django.contrib.auth.decorators import login_required
from workflows import flows,forms,models
from .forms import AlterMaker,ApprovalForm
from users.models import UserProfile
import datetime
from Cha_Flow.utils import restful
from django.contrib.auth.decorators import permission_required
# from django.contrib.auth.models import ContentType
#
#
# ContentType.objects.get_for_model()




# 添加变更并进入变更流程
@login_required
def add_alters(request):
    if request.method == 'GET':
        form = AlterMaker()
    else:
        form = AlterMaker(request.POST)
        print(form.data,"ddd")
        if form.is_valid():
            print("淼谦",form.cleaned_data)
            dic = {}
            dic["alter_title"] = form.cleaned_data.get("alter_title")
            dic['proposer'] = request.user
            dic["operator"] = UserProfile.objects.get(id=form.cleaned_data.get("operator"))
            dic["start_time"]=form.cleaned_data.get("start_time")
            dic["end_time"] = form.cleaned_data.get("end_time")
            dic["risk_level"] = form.cleaned_data.get("risk_level")
            dic["alter_type"] = form.cleaned_data.get("alter_type")
            dic["memo"] = request.POST.get("memo")

            dic["alter_effect"] = form.cleaned_data.get("alter_effect")
            dic["alter_stop_time"] = form.cleaned_data.get("alter_stop_time")
            dic["alter_stop_range"] = form.cleaned_data.get("alter_stop_range")
            dic["technical_director"] = UserProfile.objects.get(id=form.cleaned_data.get("technical_director"))
            dic["customer_director"] =  UserProfile.objects.get(id=form.cleaned_data.get("customer_director"))
            dic["technical_director_opnion"] = form.cleaned_data.get("technical_director_opnion")
            dic["committee_opnion"] = form.cleaned_data.get("committee_opnion")

            dic["implement_plan"] = form.cleaned_data.get("implement_plan")
            dic["implement_plan_time"] = form.cleaned_data.get("implement_plan_time")
            dic["implement_validate_plan"] = form.cleaned_data.get("implement_validate_plan")
            dic["implement_validate_plan_time"] = form.cleaned_data.get("implement_validate_plan_time")

            dic["back_plan"] = form.cleaned_data.get("back_plan")
            dic["back_plan_time"] = form.cleaned_data.get("back_plan_time")
            dic["back_validate_plan"] = form.cleaned_data.get("back_validate_plan")
            dic["back_validate_plan_time"] = form.cleaned_data.get("back_validate_plan_time")

            dic["yingji_plan"] = form.cleaned_data.get("yingji_plan")
            dic["yingji_plan_time"] = form.cleaned_data.get("yingji_plan_time")
            dic["yingji_validate_plan"] = form.cleaned_data.get("yingji_validate_plan")
            dic["yingji_validate_plan_time"] = form.cleaned_data.get("yingji_validate_plan_time")


            upload_alert=Alter.objects.create(**dic)
            dic_alter_desc = {}
            dic_alter_desc["alter_momo"] = form.cleaned_data.get("alter_momo")
            dic_alter_desc["change_type"] = form.cleaned_data.get("change_type")
            dic_alter_desc["approve_user"] = form.cleaned_data.get("approve_user")
            dic_alter_desc["alter_description"] = form.cleaned_data.get("alter_description")

            dic_alter_desc["other_env"] = form.cleaned_data.get("other_env")
            dic_alter_desc["alter"] = upload_alert
            alter_desc = Alter_Desc.objects.create(**dic_alter_desc)

            FlowRecord.objects.create(flow=upload_alert,step=Step.objects.filter(order=1).first(),status=3)

            return redirect(reverse("workflow:show_my_alters"))
        else:
            print(form.errors,"shishi")
    return render(request,"workflow/alter_create.html",{'form': form,"user":request.user},)


# 只保存不添加变更流程
def save_alters(request):
    if request.method == 'GET':
        form = AlterMaker()
    else:
        form = AlterMaker(request.POST)
        if form.is_valid():
            print("淼谦",form.cleaned_data)
            dic = {}
            dic["alter_title"] = form.cleaned_data.get("alter_title")
            dic['proposer'] = request.user
            dic["operator"] = UserProfile.objects.get(id=form.cleaned_data.get("operator"))
            dic["start_time"]=form.cleaned_data.get("start_time")
            dic["end_time"] = form.cleaned_data.get("end_time")
            dic["risk_level"] = form.cleaned_data.get("risk_level")
            dic["alter_type"] = form.cleaned_data.get("alter_type")
            dic["memo"] = form.cleaned_data.get("memo")

            dic["alter_effect"] = form.cleaned_data.get("alter_effect")
            dic["alter_stop_time"] = form.cleaned_data.get("alter_stop_time")
            dic["alter_stop_range"] = form.cleaned_data.get("alter_stop_range")
            dic["technical_director"] = UserProfile.objects.get(id=form.cleaned_data.get("technical_director"))
            dic["customer_director"] =  UserProfile.objects.get(id=form.cleaned_data.get("customer_director"))
            dic["technical_director_opnion"] = form.cleaned_data.get("technical_director_opnion")
            dic["committee_opnion"] = form.cleaned_data.get("committee_opnion")

            dic["implement_plan"] = form.cleaned_data.get("implement_plan")
            dic["implement_plan_time"] = form.cleaned_data.get("implement_plan_time")
            dic["implement_validate_plan"] = form.cleaned_data.get("implement_validate_plan")
            dic["implement_validate_plan_time"] = form.cleaned_data.get("implement_validate_plan_time")

            dic["back_plan"] = form.cleaned_data.get("back_plan")
            dic["back_plan_time"] = form.cleaned_data.get("back_plan_time")
            dic["back_validate_plan"] = form.cleaned_data.get("back_validate_plan")
            dic["back_validate_plan_time"] = form.cleaned_data.get("back_validate_plan_time")

            dic["yingji_plan"] = form.cleaned_data.get("yingji_plan")
            dic["yingji_plan_time"] = form.cleaned_data.get("yingji_plan_time")
            dic["yingji_validate_plan"] = form.cleaned_data.get("yingji_validate_plan")
            dic["yingji_validate_plan_time"] = form.cleaned_data.get("yingji_validate_plan_time")
            dic["alter_status"] = 1
            upload_alert=Alter.objects.create(**dic)
            dic_alter_desc = {}
            dic_alter_desc["alter_momo"] = form.cleaned_data.get("alter_momo")
            dic_alter_desc["change_type"] = form.cleaned_data.get("change_type")
            dic_alter_desc["approve_user"] = form.cleaned_data.get("approve_user")
            dic_alter_desc["alter_description"] = form.cleaned_data.get("alter_description")
            dic_alter_desc["other_env"] = form.cleaned_data.get("other_env")
            dic_alter_desc["alter"] = upload_alert
            alter_desc = Alter_Desc.objects.create(**dic_alter_desc)


            return redirect(reverse("workflow:show_my_alters"))


    return render(request,"workflow/alter_create.html",{'form': form,"user":request.user},)


# 查看已提交的变更详情
@login_required
def show_alter(request,alter_id):
    alter_object = Alter.objects.get(alter_id=alter_id)
    print(alter_object.alter_id,"继续侧写")
    return render(request,"workflow/show_alter.html",{"alter_object":alter_object})

#对被退回的或者仍处于保存状态的变更进行编辑操作
def edit_alter(request,alter_id):
    if request.method == "GET":
        obj = Alter.objects.filter(alter_id=alter_id, alter_status__in=[1,2]).first()
        # 对两个时间做初始处理
        start_time = str(obj.start_time).split("+",1)[0]
        end_time = str(obj.end_time).split("+",1)[0]
        if not obj:
            return restful.unauth('已进入流程的问题无法再次编辑')

        # initial 仅初始化，不会触发form.error验证错误
        form = AlterMaker(initial={'alter_title': obj.alter_title,'operator':obj.operator.id,
                                   'risk_level':obj.risk_level,'alter_type':obj.alter_type,
                                   'memo':obj.memo,'alter_momo':obj.alter_desc_set.first().alter_momo,
                                   'change_type':obj.alter_desc_set.first().change_type,
                                   'approve_user':obj.alter_desc_set.first().approve_user,
                                   'alter_description':obj.alter_desc_set.first().alter_description,
                                   'other_env':obj.alter_desc_set.first().other_env,'alter_effect':obj.alter_effect,
                                   'alter_stop_time':obj.alter_stop_time,'alter_stop_range':obj.alter_stop_range,
                                   'technical_director':obj.technical_director.id,
                                   'customer_director':obj.customer_director.id,
                                   'technical_director_opnion':obj.technical_director_opnion,
                                   'committee_opnion':obj.committee_opnion,'implement_plan':obj.implement_plan,
                                   'implement_plan_time':obj.implement_plan_time,
                                   'implement_validate_plan':obj.implement_validate_plan,
                                   'implement_validate_plan_time':obj.implement_validate_plan_time,
                                   'back_plan':obj.back_plan,'back_plan_time':obj.back_plan_time,
                                   'back_validate_plan':obj.back_validate_plan,
                                   'back_validate_plan_time':obj.back_validate_plan_time,'yingji_plan':obj.yingji_plan,
                                   'yingji_plan_time':obj.yingji_plan_time,
                                   'yingji_validate_plan':obj.yingji_validate_plan,
                                   'yingji_validate_plan_time':obj.yingji_validate_plan_time
                                   })

        context= {'form':form,'alter_id':alter_id,'obj':obj,"start_time":start_time,"end_time":end_time}
        return render(request,'workflow/edit_alter.html',context=context)


def update_and_submit(request,alter_id):
    if request.method == 'POST':
        form = AlterMaker(request.POST)
        if form.is_valid():
            dic = {}
            dic["alter_title"] = form.cleaned_data.get("alter_title")
            dic['proposer'] = request.user
            dic["operator"] = UserProfile.objects.get(id=form.cleaned_data.get("operator"))
            dic["start_time"] = form.cleaned_data.get("start_time")
            dic["end_time"] = form.cleaned_data.get("end_time")
            dic["risk_level"] = form.cleaned_data.get("risk_level")
            dic["alter_type"] = form.cleaned_data.get("alter_type")
            dic["memo"] = request.POST.get("memo")

            dic["alter_effect"] = form.cleaned_data.get("alter_effect")
            dic["alter_stop_time"] = form.cleaned_data.get("alter_stop_time")
            dic["alter_stop_range"] = form.cleaned_data.get("alter_stop_range")
            dic["technical_director"] = UserProfile.objects.get(id=form.cleaned_data.get("technical_director"))
            dic["customer_director"] = UserProfile.objects.get(id=form.cleaned_data.get("customer_director"))
            dic["technical_director_opnion"] = form.cleaned_data.get("technical_director_opnion")
            dic["committee_opnion"] = form.cleaned_data.get("committee_opnion")

            dic["implement_plan"] = form.cleaned_data.get("implement_plan")
            dic["implement_plan_time"] = form.cleaned_data.get("implement_plan_time")
            dic["implement_validate_plan"] = form.cleaned_data.get("implement_validate_plan")
            dic["implement_validate_plan_time"] = form.cleaned_data.get("implement_validate_plan_time")

            dic["back_plan"] = form.cleaned_data.get("back_plan")
            dic["back_plan_time"] = form.cleaned_data.get("back_plan_time")
            dic["back_validate_plan"] = form.cleaned_data.get("back_validate_plan")
            dic["back_validate_plan_time"] = form.cleaned_data.get("back_validate_plan_time")

            dic["yingji_plan"] = form.cleaned_data.get("yingji_plan")
            dic["yingji_plan_time"] = form.cleaned_data.get("yingji_plan_time")
            dic["yingji_validate_plan"] = form.cleaned_data.get("yingji_validate_plan")
            dic["yingji_validate_plan_time"] = form.cleaned_data.get("yingji_validate_plan_time")

            Alter.objects.filter(alter_id=alter_id).update(**dic)
            upload_alert = Alter.objects.get(alter_id=alter_id)
            upload_alert_desc_id=upload_alert.alter_desc_set.first().id

            dic_alter_desc = {}
            dic_alter_desc["alter_momo"] = form.cleaned_data.get("alter_momo")
            dic_alter_desc["change_type"] = form.cleaned_data.get("change_type")
            dic_alter_desc["approve_user"] = form.cleaned_data.get("approve_user")
            dic_alter_desc["alter_description"] = form.cleaned_data.get("alter_description")


            dic_alter_desc["other_env"] = form.cleaned_data.get("other_env")
            dic_alter_desc["alter"] = upload_alert
            Alter_Desc.objects.filter(id=upload_alert_desc_id).update(**dic_alter_desc)

            FlowRecord.objects.create(flow=upload_alert, step=Step.objects.filter(order=1).first(), status=3)

            return redirect(reverse("workflow:show_my_alters"))


def update_and_save(request,alter_id):
    if request.method == 'POST':
        form = AlterMaker(request.POST)
        print(form.data, "ddd")
        if form.is_valid():
            dic = {}
            dic["alter_title"] = form.cleaned_data.get("alter_title")
            dic['proposer'] = request.user
            dic["operator"] = UserProfile.objects.get(id=form.cleaned_data.get("operator"))
            dic["start_time"] = form.cleaned_data.get("start_time")
            dic["end_time"] = form.cleaned_data.get("end_time")
            dic["risk_level"] = form.cleaned_data.get("risk_level")
            dic["alter_type"] = form.cleaned_data.get("alter_type")
            dic["memo"] = request.POST.get("memo")

            dic["alter_effect"] = form.cleaned_data.get("alter_effect")
            dic["alter_stop_time"] = form.cleaned_data.get("alter_stop_time")
            dic["alter_stop_range"] = form.cleaned_data.get("alter_stop_range")
            dic["technical_director"] = UserProfile.objects.get(id=form.cleaned_data.get("technical_director"))
            dic["customer_director"] = UserProfile.objects.get(id=form.cleaned_data.get("customer_director"))
            dic["technical_director_opnion"] = form.cleaned_data.get("technical_director_opnion")
            dic["committee_opnion"] = form.cleaned_data.get("committee_opnion")

            dic["implement_plan"] = form.cleaned_data.get("implement_plan")
            dic["implement_plan_time"] = form.cleaned_data.get("implement_plan_time")
            dic["implement_validate_plan"] = form.cleaned_data.get("implement_validate_plan")
            dic["implement_validate_plan_time"] = form.cleaned_data.get("implement_validate_plan_time")

            dic["back_plan"] = form.cleaned_data.get("back_plan")
            dic["back_plan_time"] = form.cleaned_data.get("back_plan_time")
            dic["back_validate_plan"] = form.cleaned_data.get("back_validate_plan")
            dic["back_validate_plan_time"] = form.cleaned_data.get("back_validate_plan_time")

            dic["yingji_plan"] = form.cleaned_data.get("yingji_plan")
            dic["yingji_plan_time"] = form.cleaned_data.get("yingji_plan_time")
            dic["yingji_validate_plan"] = form.cleaned_data.get("yingji_validate_plan")
            dic["yingji_validate_plan_time"] = form.cleaned_data.get("yingji_validate_plan_time")

            Alter.objects.filter(alter_id=alter_id).update(**dic)
            upload_alert = Alter.objects.get(alter_id=alter_id)
            upload_alert_desc_id=upload_alert.alter_desc_set.first().id

            dic_alter_desc = {}
            dic_alter_desc["alter_momo"] = form.cleaned_data.get("alter_momo")
            dic_alter_desc["change_type"] = form.cleaned_data.get("change_type")
            dic_alter_desc["approve_user"] = form.cleaned_data.get("approve_user")
            dic_alter_desc["alter_description"] = form.cleaned_data.get("alter_description")


            dic_alter_desc["other_env"] = form.cleaned_data.get("other_env")
            dic_alter_desc["alter"] = upload_alert
            Alter_Desc.objects.filter(id=upload_alert_desc_id).update(**dic_alter_desc)

            return redirect(reverse("workflow:show_my_alters"))


def delete_my_submit_alter(request,alter_id):
    if request.method == "POST":
        obj = Alter.objects.filter(alter_id=alter_id, alter_status__in=[1, 2]).first()
        if not obj:
            return restful.unauth('已进入流程的问题无法删除')
        Alter.objects.filter(alter_id=alter_id).delete()
    return redirect(reverse("workflow:show_my_alters"))


# 我提交的变更申请的列表
@login_required
def show_my_submit_alter(request):
    current_user_id = request.user.id
    result = Alter.objects.filter(proposer_id=current_user_id).order_by('-date'). only('alter_id', 'alter_title','operator', 'date', 'alter_type')
    return render(request,"workflow/my_submit_alterlist.html",{"result":result})


# 具体变更的流程环节详情
@login_required
def alter_detail(request,flow_id):
    flow_obj = models.Alter.objects.get(alter_id=flow_id)
    return render(request,"workflow/flow_detail.html", locals())


# 需要被我(也就是我所在的角色)审批的变更流程的页面
def my_alter_approvals(request):
    flow_manager_obj = flows.FlowManger(request)
    queued_flows = flow_manager_obj.get_assigned_to_me_flowlist()
    queue_flow = queued_flows.first()
    return render(request, "workflow/my_alter_approvals.html", locals())


#对变更进行分层审批
@login_required
def alter_approve(request,record_id):
    flow_record_objective = FlowRecord.objects.get(id=record_id)
    print(flow_record_objective,"侧写")
    if request.method == "GET":
        form = ApprovalForm()
    else:
        form = ApprovalForm(request.POST)
        if form.is_valid():
            dic={}
            dic['status'] = form.cleaned_data["status"]
            print(dic['status'],"AA")

            dic['user'] = request.user
            dic['comment'] = form.cleaned_data["comment"]
            dic["step_status"] = 1
            dic['date'] = datetime.datetime.now()
            print(dic)

            z = FlowRecord.objects.filter(id=record_id,step_status=0).update(**dic)
            if not z:
                return restful.unauth("该变更已被别人审批")

            step_count = models.Step.objects.count()
            if flow_record_objective.step.order != step_count:
                if form.cleaned_data['status'] == 1:
                    flow_object= flow_record_objective.flow
                    flow_object.alter_status = 2
                    flow_object.save()
                    # new_step = Step.objects.get(order=1)
                    # FlowRecord.objects.create(flow_id=flow_record_objective.flow_id, step=new_step, status=3)
                else:
                    new_record_step_order = flow_record_objective.step.order + 1
                    new_step = Step.objects.get(order=new_record_step_order)
                    FlowRecord.objects.create(flow_id=flow_record_objective.flow_id,step=new_step,status=3)



            return redirect(reverse("workflow:my_alter_approvals"))

    return render(request,"workflow/alter_approve.html",locals())


# 作为审批者时，"我"的审批记录页
@login_required
def my_approval_records(request):
    related_steps = []
    for role in request.user.flowrole_set.all():
        related_steps.extend(role.step_set.all())

    queued_flows = models.FlowRecord.objects.filter(step__in=related_steps,user=request.user).order_by("-date")
    queue_flow = queued_flows.first()
    return render(request,"workflow/my_approval_records.html", locals())

#跳转页面，查看变更所处的实际流程,后续还会考虑数据可视化
@login_required
def alter_flow_real_time(request,record_id):
    flow_record_objective = FlowRecord.objects.get(id=record_id)
    # print("啊啊啊啊啊啊",flow_record_objective.date)
    return render(request,'workflow/alter_flow_real_time.html',locals())













