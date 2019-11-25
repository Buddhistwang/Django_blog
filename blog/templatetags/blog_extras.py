#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : blog_extras.py
# @Author  : Yangzw

from django import template
from ..models import Post, Category, Tag

register = template.Library()





# 最新文章模板标签
'''
takes_context 设置为 True 时将告诉 django，
在渲染 _recent_posts.html 模板时，
不仅传入show_recent_posts 返回的模板变量，
同时会传入父模板（即使用 {% show_recent_posts %} 模板标签的模板）
上下文（可以简单理解为渲染父模板的视图函数传入父模板的模板变量以及 django 自己传入的模板变量）。
当然这里并没有用到这个上下文，这里只是做个简单演示，如果需要用到，就可以在模板标签函数的定义中使用
context 变量引用这个上下文。
'''
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {'recent_post_list': Post.objects.all().order_by('-created_time')[:num],}


# 归档模板标签
'''
这里 Post.objects.dates 方法会返回一个列表，
列表中的元素为每一篇文章（Post）的创建时间（已去重），
且是 Python 的 date 对象，精确到月份，降序排列。
接受的三个参数值表明了这些含义，一个是 created_time ，
即 Post 的创建时间，month 是精度，order='DESC' 表明降序排列（即离当前越近的时间越排在前面）
。例如我们写了 3 篇文章，分别发布于 2019 年 2 月 21 日、2019 年 3 月 25 日、2019 年 3 月 28 日
，那么 dates 函数将返回 2019 年 3 月 和 2019 年 2 月这样一个时间列表，且降序排列，从而帮助我们实现按月归档的目的。
'''
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {'date_list': Post.objects.dates('created_time', 'month', order='DESC'),}


# 分类模板标签
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {'category_list': Category.objects.all(), }


# 标签云模板标签
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {'tag_list': Tag.objects.all(),}
