from django.db import models
from django.db.models import Q
from django.urls import reverse

from autoslug import AutoSlugField
from taggit_selectize.managers import TaggableManager

from categories.models import Category


class GoodQuerySet(models.QuerySet):
    def list(self, query_dict=None):
        if query_dict is None:
            query_dict = {}
        queryset = self
        cat_id = query_dict.get('cat_id')
        if cat_id:
            queryset = queryset.filter(category__id=cat_id).distinct()
        tags = query_dict.get('tags')
        if tags:
            tags = tags.split(',')
            queryset = queryset.filter(tags__name__in=tags).distinct()
        query = query_dict.get('query')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query)).distinct()
        return queryset


def get_slug(instance):
    return f'{instance.category.name}-{instance.name}'


class Good(models.Model):
    class Meta:
        ordering = (
            '-price',
            'name',
        )
        unique_together = (
            'category',
            'name',
            'price',
        )
        verbose_name = 'good'
        verbose_name_plural = 'goods'

    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='goods')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='In stock')
    price = models.FloatField()
    tags = TaggableManager(blank=True)
    slug = AutoSlugField(
        populate_from=get_slug,
        unique=True
    )
    objects = GoodQuerySet.as_manager()

    def __str__(self):
        return self.name if self.in_stock else f'{self.name} (out of stock)'

    def get_in_stock(self):
        return '+' if self.in_stock else ''

    def get_absolute_url(self):
        return reverse('goods:detail', kwargs={'slug': self.slug})
