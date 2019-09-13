from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from .models import Ask_Question
from .forms import QuestionMaker,QuestionKill
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def show_index(request):
    current_user_id = request.user.id
    print("hahah",current_user_id)
    result = Ask_Question.objects.filter(user_id=current_user_id).order_by('status'). \
        only('title', 'status', 'ctime', 'processer')
    print("eee",result)
    return render(request,"question_record/index.html",{"result":result})

import datetime

@login_required
def create_question(request):
    if request.method == 'GET':
        form = QuestionMaker()
    else:
        form = QuestionMaker(request.POST)
        if form.is_valid():
            # title,content
            # form.cleaned_data
            dic = {}
            dic['user_id'] = request.user.id # session中获取
            dic['ctime'] = datetime.datetime.now()
            dic['status'] = 1
            dic.update(form.cleaned_data)
            print(dic,"aaa")
            Ask_Question.objects.create(**dic)
            return redirect('/questions/index/')
    return render(request, 'question_record/question_create.html',{'form':form})

@login_required
def edit_question(request,nid):

    if request.method == "GET":
        obj = Ask_Question.objects.filter(id=nid, status=1).only('id', 'title', 'detail').first()
        if not obj:
            return HttpResponse('已处理中的问题无法修改..')
        # initial 仅初始化，不会触发form.error验证错误
        form = QuestionMaker(initial={'title': obj.title,'detail': obj.detail})
        # 执行error会进行验证
        return render(request,'question_record/question_edit.html',{'form':form,'nid':nid})
    else:
        form = QuestionMaker(data=request.POST)
        user = Ask_Question.objects.filter(id=nid).first().user
        if form.is_valid() and request.user == user:
            # 就update而言，v是指受响应的行数，status=1是关键，防止多人重复更改
            v = Ask_Question.objects.filter(id=nid, status=1).update(**form.cleaned_data)
            if not v:
                return HttpResponse('问题已经被解决')
            else:
                return redirect('/questions/index/')
        return render(request, 'question_record/question_edit.html', {'form': form, 'nid': nid})

@login_required
def question_kill_list(request):
    current_user_id=request.user.id
    result=Ask_Question.objects.filter(Q(processer_id=current_user_id)|Q(status=1)).order_by("status")
    return render(request,"question_record/question_kill_list.html",{"result":result})

@login_required
def question_kill(request,nid):
    if request.method=="GET":
        v=Ask_Question.objects.filter(id=nid,status=1).update(processer_id=request.user.id,status=2) \
          or Ask_Question.objects.filter(processer_id=request.user.id,id=nid).count()#第二个filter是指过去抢到的问题处理单
        if not v:
            return HttpResponse("其他同事已经在你点击时候处理")
        obj=Ask_Question.objects.filter(id=nid).first()
        form=QuestionKill(initial={"title":obj.title,"detail":obj.detail,"solution":obj.solution})

        return render(request,"question_record/question_kill.html",{"form":form,"nid":nid,"z":obj.detail})
    else:
        #确认当前用户在做操作
        ret=Ask_Question.objects.filter(id=nid,processer_id=request.user.id,status=2).count()
        print(ret,"侧写师")
        if not ret:
            return HttpResponse("此处返还json")
        form=QuestionKill(request.POST)
        if form.is_valid():
            dic={}
            dic["status"]=3
            dic["solution"]=form.cleaned_data.get("solution")
            dic["ptime"]=datetime.datetime.now()
            Ask_Question.objects.filter(id=nid,processer_id=request.user.id,status=2).update(**dic)
            return redirect("/questions/kill-list")
        obj=Ask_Question.objects.filter(id=nid).first()
        return render(request, "question_record/question_kill.html", {"obj":obj,"form": form, "nid": nid})


