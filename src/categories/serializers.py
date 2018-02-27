#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from categories.models import Category
from goods.models import Good
from goods.serializers import GoodUpdateSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'goods')

    goods = GoodUpdateSerializer(many=True)

    def create(self, validated_data):
        goods_data = validated_data.pop('goods', None)
        category = Category.objects.create(**validated_data)
        for good_data in goods_data:
            Good.objects.create(category=category, **good_data)
        return category

    def update(self, instance, validated_data):
        if 'goods' in validated_data:
            goods_data = validated_data.pop('goods')
            if goods_data:
                goods_to_delete = instance.goods.exclude(pk__in=[item.get('id', None) for item in goods_data])

                for item in goods_data:
                    item_id = item.get('id', None)
                    if item_id:
                        good_item = Good.objects.get(id=item_id, category=instance)
                        good_item.name = item.get('name', good_item.name)
                        good_item.price = item.get('price', good_item.price)
                        good_item.save()
                    else:
                        Good.objects.create(category=instance, **item)
            else:
                goods_to_delete = instance.goods.all()
            # Delete goods which are not exists in validated_data
            if goods_to_delete:
                goods_to_delete.delete()

        super(CategorySerializer, self).update(instance, validated_data)
        return instance
