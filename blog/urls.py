#!/usr/bin/python
# -*- coding: utf-8 -*-
# @File    : urls.py
# @Author  : Yangzw

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]