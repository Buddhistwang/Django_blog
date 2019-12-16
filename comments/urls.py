#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : urls.py
# @Author  : Yangzw

from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
