from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('index/',index),
    path('register/',register),
    path('login/',login),
    path('article_list/',article_list),
    re_path('article_list/(?P<status>[01])/(?P<page>\d+)',article_list),
    re_path('art_status/(?P<status>\w+)/(?P<id>\d+)',art_status),
    path('personal_center/',personal_center),
    path('article_add/',article_add),

]