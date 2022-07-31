# Create your views here.
from django.shortcuts import render, redirect
from article.models import ArticlePost
import markdown
from django.http import HttpResponse
from article.forms import ArticlePostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator  # 分页模块
from django.contrib.auth.views import login_required


def article_list(request):
    if request.GET.get('order') == 'total_views':
        article_list = ArticlePost.objects.all().order_by('-total_views')
        order = 'total_views'
    else:
        article_list = ArticlePost.objects.all()
        order = 'normal'

    # 每页显示一片文章
    paginator = Paginator(article_list, 1)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {'articles': articles, 'order': order}
    return render(request, 'article/list.html', context)


# 文章详情
def article_detail(request, id=None):
    # 取出相应文章
    article = ArticlePost.objects.get(id=id)
    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    # 将 markdown 的语法渲染成html样式
    article.body = markdown.markdown(
        article.body,  # 需要渲染的文本
        extensions=[
            # 包含 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ]
    )
    # 需要传递给模版的对象
    context = {'article': article}
    # 载入模版， 并返回context对象
    return render(request, 'article/detail.html', context)


# 写文章的视图
def article_create(request):
    # 判断用户是否提交数据
    if request.method == 'POST':
        # 将提交的数据赋值到表单实例
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足数据模型
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交
            new_article = article_post_form.save(commit=False)
            # 指定目前登陆的用户作为作者
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            # 完成后返回到文章列表
            return redirect('article:article_list')
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        # 返回模型
        return render(request, 'article/create.html', context)


# 删除文章
@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.user != article.author:
        return HttpResponse("抱歉，你无权删除这篇文章")
    if request.method == "POST":
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")


# 更新文章
@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    # 过滤非作者用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章")

    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        context = {'article': article, 'article_post_form': article_post_form}
        return render(request, 'article/update.html', context)
