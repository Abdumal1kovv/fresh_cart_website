from django.test import TestCase

from orders.models import Category

# pytest, unittest

from django.test import TestCase


class CategoryTestCase(TestCase):

    def setUp(self):
        Category.objects.create(name='category-1', slug='category-1')
        Category.objects.create(name='category-2', slug='category-2')

    def test_create_category(self):
        category = Category.objects.create(name='category-new', slug='category-new')

        self.assertEqual(category.id, 3)
        self.assertEqual(category.name, 'category-new1')
        self.assertEqual(category.slug, 'category-new')
