# -*- coding: utf-8 -*-
# @Time : 2022/7/29 20:41
# @Author : proudzhao
from django.urls import path
from article import views

app_name = 'article'  # 正在部署的应用名称

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    # path新语法用尖括号<>定义需要传递的参数。这里需要传递名叫id的整数到视图函数中去。
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]
