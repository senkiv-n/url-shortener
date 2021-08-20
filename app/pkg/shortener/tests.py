from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from model_mommy.recipe import Recipe
from app.pkg.shortener.models import ShortenedUrl


class ShortenerTestCase(APITestCase):
    create_shortener_url = reverse('shortener-list')
    urls_count_url = reverse('shortener-urls-count')
    most_popular_urls = reverse('most-popular-list')

    url = 'https://www.google.com.ua/'
    url2 = 'https://www.amazon.com/'
    url3 =  'https://www.google.com.ua/test/'

    def test_create_shortener_url_201(self):
        response = self.client.post(self.create_shortener_url, data={'url': self.url})
        self.assertTrue(len(response.data['shortened_url']) > 0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_create_shortener_invalid_url_400(self):
        response = self.client.post(self.create_shortener_url, data={'url': 'sdklfj'})
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_urls_count(self):
        self.client.post(self.create_shortener_url, data={'url': self.url})
        self.client.post(self.create_shortener_url, data={'url': self.url2})
        response = self.client.get(self.urls_count_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['shortened_urls_count'], 2)

    def test_get_most_popular(self):
        Recipe(ShortenedUrl).make(url=self.url, short_path='aaa')
        Recipe(ShortenedUrl).make(url=self.url2, short_path='bbb')
        Recipe(ShortenedUrl).make(url=self.url3, short_path='ccc')
        response = self.client.get(self.most_popular_urls)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.count(), 2)
