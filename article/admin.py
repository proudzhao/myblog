from django.contrib import admin

# Register your models here.
from django.contrib import admin
from article.models import ArticlePost

# 注册 ArticlePost 到 admin 中
admin.site.register(ArticlePost)
