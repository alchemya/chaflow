

# Create your views here.
import django
from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.db.models import Q
from . import permissions
from Cha_Flow.utils import restful
from django.views.generic import View
from django.contrib.auth.hashers import make_password
from .forms import ChangePwdForm,EditUserForm

#设置账户登录可以以用户名或者邮箱
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

#登录
# @permissions.check_permission
def acc_login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)

        if user is not None:
            if user.valid_end_time: #设置了end time
                if django.utils.timezone.now() > user.valid_begin_time and django.utils.timezone.now()  < user.valid_end_time:
                    login(request,user)
                    request.session.set_expiry(60*24*60*7)
                    #print 'session expires at :',request.session.get_expiry_date()
                    return redirect('/')
                else:
                    return render(request,'login.html',{'login_err': '账户没有权限，请联系it部门'})
            elif django.utils.timezone.now() > user.valid_begin_time:
                    login(request,user)
                    request.session.set_expiry(60*60*24*7)
                    return redirect('/')

        else:
            return render(request,'login.html',{'login_err': '用户名或者密码错误'})
    else:
        return render(request, 'login.html')

#登出
def acc_logout(request):
    logout(request)
    return redirect('/login/')


def myself(request):
    user_count = get_object_or_404(UserProfile,id=request.user.id)
    return render(request,'user/my_self_page.html',{ 'user':user_count })



def myself_edit(request):
    if request.method == "GET":
        user = get_object_or_404(UserProfile, id=request.user.id)
        form = EditUserForm(initial={'postion':user.postion,'email':user.email,'mobile':user.mobile,
                                     'memo':user.memo,'company':user.company,'department':user.department})

        return render(request,'user/edit_my_information.html',{'form':form })
    else:
        form = EditUserForm(request.POST)
        if form.is_valid():
            UserProfile.objects.filter(id=request.user.id).update(**form.cleaned_data)
            return redirect(reverse("users:my_information"))



def user_info(request,user_id):
    user = get_object_or_404(UserProfile,id=user_id)
    return render(request,'user/user_info.html',{'user':user})




#图片剪贴器
def my_image(request):
    if request.method == 'POST':
        img=request.POST['img']
        userinfo = UserProfile.objects.get(id=request.user.id)
        userinfo.photo= img
        userinfo.save()
        return restful.success()
    else:
        return render(request,'user/imagecrop.html')



class ChangepwdView(View):
    def post(self,request):
        change_pwd_form=ChangePwdForm(request.POST)
        if change_pwd_form.is_valid():
            pwd1=change_pwd_form.cleaned_data.get('password1')
            pwd2=change_pwd_form.cleaned_data.get('password2')
            email=request.POST.get('email','')
            active_code = request.POST.get('active_code')
            active_code = EmailVerifyRecord.objects.filter(code=active_code).first()

            if pwd1!=pwd2:
                return render(request,'password_reset.html',{'msg':'密码不一致','email':email})

            if active_code.email == email:
                user=UserProfile.objects.get(email=email)
                user.password=make_password(pwd1)
                user.save()
                return render(request, 'login.html')
            else:
                return render(request,'password_reset.html',{'msg':'邮箱内激活链接无效'})

        else:
            email=request.POST.get('email','')
            active_code = request.POST.get('active_code')
            return render(request,'password_reset.html',{'email':email,'change_pwd_form':change_pwd_form,'active_code':active_code})