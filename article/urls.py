# -*- coding: utf-8 -*-
# @Time : 2022/7/29 20:41
# @Author : proudzhao
from django.urls import path
from article import views

app_name = 'article'  # 正在部署的应用名称

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
]
