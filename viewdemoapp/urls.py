from viewdemoapp.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path


urlpatterns=[
     path('index',index),
]
