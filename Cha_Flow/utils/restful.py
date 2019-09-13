__author__ = 'yuchen'
__date__ = '2019/1/29 10:06'

#encoding: utf-8
from django.http import JsonResponse

class HttpCode(object):
    ok = 200
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500

# {"code":400,"message":"","data":{}}



def restful_result(code=HttpCode.ok,message="",data=None,kwargs=None):
    json_dict={"code":code,"message":message,"data":data}
    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)



def success(message='',data=None):
    return restful_result(HttpCode.ok,message=message,data=data)


def params_error(message="",data=None):
    return restful_result(code=HttpCode.paramserror,message=message,data=data)

def unauth(message="",data=None):
    return restful_result(code=HttpCode.unauth,message=message,data=data)

def method_error(message='',data=None):
    return restful_result(code=HttpCode.methoderror,message=message,data=data)

def server_error(message='',data=None):
    return restful_result(code=HttpCode.servererror,message=message,data=data)

