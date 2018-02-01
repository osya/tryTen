#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from goods.models import Category, Good


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

        super(self.__class__, self).update(instance, validated_data)
        return instance
