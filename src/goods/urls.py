#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from goods.views import GoodList, GoodDetail, GoodUpdate, GoodDelete, GoodCreate

urlpatterns = [
    url(r'^$', GoodList.as_view(), name='list'),
    url(r'^(?P<slug>\d+)/$', GoodDetail.as_view(), name='detail'),
    url(r'^(?P<slug>\d+)/update/$', GoodUpdate.as_view(), name='update'),
    url(r'^(?P<slug>\d+)/delete/$', GoodDelete.as_view(), name='delete'),
    url(r'^create/$', GoodCreate.as_view(), name='create'),
]
