#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from goods.views import GoodCreate, GoodDelete, GoodDetail, GoodList, GoodUpdate, GoodViewSet
from tryTen.urls import ROUTER

app_name = 'goods'

ROUTER.register(r'goods', GoodViewSet, base_name='good')

urlpatterns = [
    path('', GoodList.as_view(), name='list'),
    path('create/', GoodCreate.as_view(), name='create'),
    path('<slug:slug>/', GoodDetail.as_view(), name='detail'),
    path('<slug:slug>/update/', GoodUpdate.as_view(), name='update'),
    path('<slug:slug>/delete/', GoodDelete.as_view(), name='delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)
