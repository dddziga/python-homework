from django.test import TestCase
from django.urls import reverse
from .models import Category, Brand, Key

class CatalogTests(TestCase):

    def setUp(self):
        # Создаем тестовые данные
        self.category = Category.objects.create(name='Electronics')
        self.brand = Brand.objects.create(name='Samsung', image='brand.jpg')
        self.key = Key.objects.create(
            name='Galaxy S21',
            brand=self.brand,
            category=self.category,
            price=799.99,
            description='Latest Samsung smartphone',
            stock=50,
            image='key.jpg'
        )

    def tearDown(self):
        # Удаляем тестовые данные
        self.key.delete()
        self.brand.delete()
        self.category.delete()

    def test_main_page_context(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Go to Catalog')
        self.assertTemplateUsed(response, 'catalog/index.html')

    def test_category_list_view_context(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/category_list.html')
        self.assertIn('categories', response.context)
        self.assertEqual(len(response.context['categories']), 1)
        self.assertEqual(response.context['categories'][0], self.category)

    def test_brand_list_view_context(self):
        response = self.client.get(reverse('brand_list', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/brand_list.html')
        self.assertIn('brands', response.context)
        self.assertEqual(len(response.context['brands']), 1)
        self.assertEqual(response.context['brands'][0], self.brand)

    def test_key_list_view_context(self):
        response = self.client.get(reverse('key_list', args=[self.category.id, self.brand.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/key_list.html')
        self.assertIn('keys', response.context)
        self.assertEqual(len(response.context['keys']), 1)
        self.assertEqual(response.context['keys'][0], self.key)

    def test_key_detail_view_context(self):
        response = self.client.get(reverse('key_detail', args=[self.category.id, self.brand.id, self.key.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/key_detail.html')
        self.assertIn('key', response.context)
        self.assertEqual(response.context['key'], self.key)
