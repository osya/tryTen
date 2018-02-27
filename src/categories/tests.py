from django.test import TestCase

import factory

from categories.models import Category


# pragma pylint: disable=R0903
class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'raw category name'
    description = 'raw category description'


# pragma pylint: enable=R0903


class CategoryTests(TestCase):
    def test_str(self):
        category = CategoryFactory()
        self.assertEqual(1, Category.objects.count())
        self.assertEqual('raw category name', category.name)
