from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from article.models import ArticlePost
from django.shortcuts import render


def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模版(templates)的对象
    context = {'articles': articles}
    # render 函数: 载入模版，并返回context对象
    return render(request, 'article/list.html', context)
