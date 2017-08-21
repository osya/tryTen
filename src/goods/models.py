from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from taggit_selectize.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class GoodQuerySet(models.QuerySet):
    def list(self, query_dict={}):
        queryset = self
        cat_id = query_dict.get('cat_id')
        if cat_id:
            queryset = queryset.filter(category__id=self.cat_id).distinct()
        tags = query_dict.get('tags')
        if tags:
            tags = tags.split(',')
            queryset = queryset.filter(tags__name__in=tags).distinct()
        q = query_dict.get('q')
        if q:
            queryset = queryset.filter(
                    Q(name__icontains=q) |
                    Q(description__icontains=q)).distinct()
        return queryset


class Good(models.Model):
    class Meta:
        ordering = ('-price', 'name',)
        unique_together = ('category', 'name', 'price',)
        verbose_name = 'good'
        verbose_name_plural = 'goods'

    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    description = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='In stock')
    price = models.FloatField()
    tags = TaggableManager(blank=True)

    objects = GoodQuerySet.as_manager()

    def __str__(self):
        return self.name if self.in_stock else f'{self.name} (out of stock)'

    def get_in_stock(self):
        return '+' if self.in_stock else ''

    def get_absolute_url(self):
        return reverse('goods:detail', kwargs={'pk': self.pk})
