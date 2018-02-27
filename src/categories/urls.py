#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.urlpatterns import format_suffix_patterns

from categories.views import CategoryViewSet
from tryTen.urls import ROUTER

app_name = 'categories'

ROUTER.register(r'categories', CategoryViewSet, base_name='category')

urlpatterns = []

urlpatterns = format_suffix_patterns(urlpatterns)
