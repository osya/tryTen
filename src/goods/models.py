from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name if self.in_stock else f'{self.name} (out of stock)'

    def get_is_stock(self):
        return '+' if self.in_stock else ''
