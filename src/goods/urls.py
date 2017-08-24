#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from goods.views import GoodList, GoodDetail, GoodUpdate, GoodDelete, GoodCreate, GoodListApi, GoodDetailApi, \
    CategoryListApi, CategoryDetailApi

goods_api_patterns = [
    url(r'^$', GoodListApi.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', GoodDetailApi.as_view(), name='detail'),
]

goods_patterns = [
    url(r'^$', GoodList.as_view(), name='list'),
    url(r'^api/', include(goods_api_patterns, namespace='api')),
    url(r'^create/$', GoodCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', GoodDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', GoodUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', GoodDelete.as_view(), name='delete'),
]

cats_patterns = [
    url(r'^api/$', CategoryListApi.as_view(), name='list'),
    url(r'^api/(?P<pk>\d+)/$', CategoryDetailApi.as_view(), name='detail'),
]

urlpatterns = [
    url(r'^$', GoodList.as_view(), name='list'),
    url(r'^cats/', include(cats_patterns, namespace='cats')),
    url(r'^goods/', include(goods_patterns, namespace='goods')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
