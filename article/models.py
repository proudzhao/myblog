from django.db import models

# Create your models here.
from django.db import models
# 导入内建的User模型
from django.contrib.auth.models import User
# timezone 用于处理时间相关的业务
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from PIL import Image


class ArticleColumn(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# 博客文章数据类型
class ArticlePost(models.Model):
    # 文章作者。 外键  参数 on_delete 用于指定数据删除方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题。 字符串字段
    title = models.CharField(max_length=100)
    # 文章栏目
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    # 文章标签
    tags = TaggableManager(blank=True)
    # 文章标题图
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
    # 文章正文。 保存大量文本使用 TextField
    body = models.TextField()
    # 文章创建时间。 参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # 文章更新时间。 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)
    # 浏览量
    total_views = models.PositiveIntegerField(default=0)

    # 内部类。 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # ordering 是元组，括号中只含一个元素时末尾要加一个逗号
        ordering = ('-created',)  # 这里是以创建时间倒序排列

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # 将文章标题返回
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    def save(self, *args, **kwargs):
        article = super(ArticlePost, self).save(*args, **kwargs)
        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article
