#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?:category/(?P<cat_id>\d+)/)?(?:page/(?P<page>\d+))?$', views.GoodList.as_view(), name='list'),
    url(r'^good/(?P<pk>\d+)/$', views.GoodDetail.as_view(), name='detail'),
    url(r'^create/(?:category/(?P<cat_id>\d+)/)?$', views.GoodCreate.as_view(), name='create'),
]
