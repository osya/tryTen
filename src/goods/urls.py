#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.GoodList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.GoodDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update$', views.GoodUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete$', views.GoodDelete.as_view(), name='delete'),
    url(r'^create$', views.GoodCreate.as_view(), name='create'),
]
