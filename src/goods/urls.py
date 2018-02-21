#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from goods.views import CategoryViewSet, GoodCreate, GoodDelete, GoodDetail, GoodList, GoodUpdate, GoodViewSet
from tryTen.urls import ROUTER

router = DefaultRouter()
router.register(r'goods', GoodViewSet, base_name='good')
router.register(r'categories', CategoryViewSet, base_name='category')

ROUTER.register(r'goods', GoodViewSet, base_name='good')
ROUTER.register(r'categories', CategoryViewSet, base_name='category')

goods_patterns = [
    url(r'^$', GoodList.as_view(), name='list'),
    url(r'^create/$', GoodCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', GoodDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', GoodUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', GoodDelete.as_view(), name='delete'),
]
urlpatterns = [
    url(r'^$', GoodList.as_view(), name='list'),
    url(r'^goods/', include(goods_patterns, namespace='goods')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
