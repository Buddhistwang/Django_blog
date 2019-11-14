from django.shortcuts import render

from django.http import HttpResponse
from .models import Post


def index(request):
    # return HttpResponse('欢迎来到我的博客首页')
    # title和welcome直接传到index.html上直接使用
    context = {'title': '博客首页', 'welcome': '欢迎来到我的博客首页'}

    # 使用模板操作数据库，取到所有数据，然后使用order_by插入时间排序。'后插入的显示在前面'
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
