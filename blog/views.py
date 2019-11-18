import re
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post



# 博客主页
def index(request):
    # return HttpResponse('欢迎来到我的博客首页')
    # title和welcome直接传到index.html上直接使用
    context = {'title': '博客首页', 'welcome': '欢迎来到我的博客首页'}

    # 使用模板操作数据库，取到所有数据，然后使用order_by插入时间排序。'后插入的显示在前面'
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 博客详情页,导入系统的404页面，如果文章存在就显示，不存在就返回404页面
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 引入markdown
    # extra 本身包含很多基础拓展，而
    # codehilite 是语法高亮拓展，这为后面的实现代码高亮功能提供基础
    # toc 允许自动生成目录
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 'markdown.extensions.toc',
        # 美化锚点
        TocExtension(slugify=slugify),
    ])

    post.body = md.convert(post.body)
    # 判断是是否为空
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={'post': post})


