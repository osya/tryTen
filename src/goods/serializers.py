#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from goods.models import Good


class GoodSerializer(serializers.ModelSerializer):
    """
        This serializer used for GoodViewSet
    """

    class Meta:
        model = Good
        fields = ('id', 'name', 'category', 'price')


class GoodUpdateSerializer(serializers.ModelSerializer):
    """
        This serializer used for CategorySerializer to be able to create new Goods during Category partial update
    """

    class Meta:
        model = Good
        # According to 'category' field, I suppose that during updating Category it will be not possible to change
        # category for a good
        fields = ('id', 'name', 'price')

    # To be possible to make Category partial update with creating new goods Good.id field should be not read_only
    # It is read_only by default as a PK
    id = serializers.IntegerField(label='ID')
