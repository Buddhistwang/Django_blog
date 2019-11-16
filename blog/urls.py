#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : urls.py
# @Author  : Yangzw

from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    # 博客详情页
    path('posts/<int:pk>/', views.detail, name='detail')
]