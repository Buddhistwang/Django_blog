#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : comments_extras.py
# @Author  : Yangzw

from django import template
from ..forms import CommentForm

register = template.Library()

# 自定义评论模板标签
@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {'form': form, 'post': post, }


# 显示评论内容
@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }
