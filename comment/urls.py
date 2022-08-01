# -*- coding: utf-8 -*-
# @Time : 2022/8/1 14:07
# @Author : proudzhao
from django.urls import path
from comment import views


app_name = 'comment'

urlpatterns = [
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]