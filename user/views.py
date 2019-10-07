from django.shortcuts import render
from article.models import *
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.

def base(reqeuest):
    return render(reqeuest,'user/base.html')

def index(request):
    article_user=LoginUser.objects.all()
    article=Article.objects.order_by('art_date')[:6]
    popular_article=Article.objects.filter(art_recommend=1).all()[:3]

    return render(request,'user/index.html',locals())

def blog_single(request):
    # article_list=Article.objects.get(id=int(id))
    return render(request,'user/blog-single.html',locals())

def category(request):
    return render(request,'user/category.html',locals())

def contact(request):
    return render(request,'user/contact.html',locals())

def about(request):
    return render(request,'user/about.html',locals())
