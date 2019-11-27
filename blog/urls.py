#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : urls.py
# @Author  : Yangzw

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    # 博客详情页路由
    path('posts/<int:pk>/', views.detail, name='detail'),
    # 归档路由
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    # 分类路由
    path('categories/<int:pk>/', views.category, name='category'),
    # 标签路由
    path('tag/<int:pk>/', views.tag, name='tag')
]
