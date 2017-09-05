#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from goods.models import Category, Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('id', 'name', 'category')
        # TODO: How to use category name instead of category id here?


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'goods')

    goods = GoodSerializer(many=True)
