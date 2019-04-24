#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xinming Hou
@license: (C) Copyright 2017-2018, CCNT of Zhejiang Unversity.
@contact: houxinming.chn@foxmail.com
@file: urls.py
@time: 2019/03/22 5:56 PM
@description:
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editor/', views.editor),
    # path('submit_code/',views.submit_code),
    path('monitor/', views.monitor),
    path('deploy/', views.deploy),
    path('training/', views.training),
    path('docs/',views.docs),
    path('case/',views.case),

    path('step_intro/',views.step_intro),
    path('select_tem/',views.select_tem),

    path('ide_editor/',views.ide_editor),

    path('copy_tem/',views.copy_tem),

    path('config_sub/',views.config_sub),

    path('submit_job/',views.submit_job),

    path('view_jobs/',views.view_jobs),

    path('test/',views.test_page),


]