#!/usr/bin/env python
# _*_coding:utf-8_*_
__author__ = 'Richie'
from django.conf.urls import include, url
from web_manage.views import home
from web_manage.views import account


urlpatterns = [
    url(r'account/checkcode/$', account.check_code),
    url(r'account/login/$', account.login),
    url(r'home/index/$', home.index),
    url(r'richie/$', account.richie),
]