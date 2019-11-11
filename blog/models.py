from django.db import models
# Django后台管理系统的用户，不是自己定义的
from django.contrib.auth.models import User

# 博客分类
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='分类名')

    def __str__(self):
        return self.name
# 博客标签
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签名')

    def __str__(self):
        return self.name

# 博客文章
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70, verbose_name='文章标题')
    # 正文
    body = models.TextField(verbose_name='文章正文')
    # 创建时间和修改时间
    created_time = models.DateTimeField(verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='修改时间')
    # 文章摘要 blank=True 允许为空
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类 on_delete=models.CASCADE 参数是关联删除 一对多
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 标签 多对多，一个文章可以有多个标签，
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者 一对多，一个作者可以写很多文章，
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title