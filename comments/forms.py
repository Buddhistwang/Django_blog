#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : forms.py
# @Author  : Yangzw

from django import forms
from .models import Comment

# 评论表单类。
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 需要的字段，评论者，邮箱网址和评论内容
        fields = ['name', 'email', 'url', 'text']