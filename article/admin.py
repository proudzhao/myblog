from django.contrib import admin

# Register your models here.
from django.contrib import admin
from article.models import ArticlePost, ArticleColumn

# 注册 ArticlePost 到 admin 中
admin.site.register(ArticlePost)
# 注册文章栏目
admin.site.register(ArticleColumn)
