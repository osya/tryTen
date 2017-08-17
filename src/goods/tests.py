from django.test import TestCase
from goods.models import Category, Good


class CategoryTests(TestCase):
    def test_str(self):
        c = Category(name='MyName', description='MyDescription')
        self.assertEqual(str(c), 'MyName')


class GoodTests(TestCase):
    def test_str(self):
        g = Good(name='MyName', description='MyDescription', in_stock=True)
        self.assertEqual(str(g), 'MyName')
