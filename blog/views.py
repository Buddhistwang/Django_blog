from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # return HttpResponse('欢迎来到我的博客首页')
    # title和welcome直接传到index.html上直接使用
    context = {'title':'博客首页', 'welcome':'欢迎来到我的博客首页'}
    return render(request, 'blog/index.html', context)