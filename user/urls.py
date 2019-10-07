from django.urls import path,re_path
from .views import *


urlpatterns = [
    path('base/',base),
    path('index/',index),
    path('blog_single/',blog_single),
    # re_path('blog_single/(?P<id>\d+)',blog_single),
    path('category/',category),
    path('contact/',contact),
    path('about/',about),

]