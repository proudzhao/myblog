# -*- coding: utf-8 -*-
# @Time : 2022/7/30 13:41
# @Author : proudzhao
from django.urls import path
from userprofile import views


app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
]