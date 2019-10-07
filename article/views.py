from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from article.models import *
from django.core.paginator import Paginator
# Create your views here.

#加密
def setpwd(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

#登录装饰器
def loginDecorator(func):
    '''
    1.获取cookies中的username 和 email
    2.判断username 和email
    3.如果成功 跳转主页
    4.如果失败 跳转登录页
    :param func:
    :return:
    '''
    def inner(request,*args,**kwargs):
        email=request.COOKIES.get("email")
        session_email=request.session.get("email")

        if email and session_email and email==session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/article/login/')

    return inner

#注册
@loginDecorator
def register(request):
    if request.method=='POST':
        err=""
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if email:
            user_info=LoginUser.objects.filter(email=email).first()
            if not user_info:
                user=LoginUser()
                user.username=username
                user.email=email
                user.password=setpwd(password)
                user.save()
                return render(request,'article/login.html',locals())
            else:
                err='邮箱已经存在 请登录'
        else:
            err="邮箱不能为空"
    return render(request,'article/register.html',locals())


def login(request):
    if request.method=='POST':
        err=''
        email=request.POST.get('email')
        password=request.POST.get('password')
        if email:
            user=LoginUser.objects.filter(email=email).first()
            if user:
                if user.password==setpwd(password) and user.email==email:
                    response=HttpResponseRedirect('/article/index/')
                    response.set_cookie('email',user.email)
                    request.session['email']=user.email
                    return response
                else:
                    err='密码错误或者张航不存在'
            else:
                err='用户不存在'
        else:
            err='邮箱不存在'
    return render(request,'article/login.html',locals())


@loginDecorator
def index(request):
    return render(request,'article/index.html',locals())

def logout(request):
    response=HttpResponseRedirect('/article/login/')
    key=request.COOKIES.keys()
    for one in key:
        response.delete_cookie(one)
    del request.session['email']
    return response

#文章列表并分页
def article_list(request,status,page=1):
    page=int(page)
    if status=="0":
        #下架文章
        art_obj=Article.objects.filter(art_status=0).order_by("art_date")
    else:
        #上架商品
        art_obj=Article.objects.filter(art_status=1).order_by("art_date")
    art_all=Paginator(art_obj,6)
    art_list=art_all.page(page)

    return render(request,'article/article_list.html',locals())
#上下架文章
def art_status(request,status,id):
    id=int(id)
    art=Article.objects.get(id=id)
    if status=='up':
        art.art_status=1
    else:
        art.art_status=0
    art.save()
    url=request.META.get("HTTP_REFERER","/article/article_list/1/1/")
    return HttpResponseRedirect(url)

#个人中心
@loginDecorator
def personal_center(request):
    user_id=request.COOKIES.get("userid")
    user=LoginUser.objects.filter(id=user_id).first()
    if request.method=="POST":
        data=request.POST
        user.username=data.get("username")
        user.email=data.get("email")
        user.age=data.get("age")
        user.gender=data.get("gender")
        user.photo=data.get("photo")
        user.address=data.get("address")
        user.save()
    return render(request,'article/personal_center.html',locals())

def article_add(request):
    art_type=Type.objects.all()
    if request.method=="POST":
        data=request.POST
        article=Article()
        article.art_title=data.get("art_title")
        article.art_content=data.get("art_content")
        article.art_date=data.get("art_date")
        article.art_des=data.get("art_des")
        article.art_picture=request.FILES.get("picture")
        article.art_status=1
        article.save()
    return render(request,'article/article_add.html',locals())




