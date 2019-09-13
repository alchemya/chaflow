__author__ = 'yuchen'
__date__ = '2018/12/4 02:14'

#实现了登录用户只能操作自己创建的项目的操作
def view_my_own_customers(request):
    print("running permisionn hook check.....")
    # 下面的代码我没写完
    if str(request.user.id) == request.GET.get('yuchen'):
        print("访问自己创建的用户,允许")
        return True
    else:
        return False