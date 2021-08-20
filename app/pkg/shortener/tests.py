from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from model_mommy.recipe import Recipe
from app.pkg.shortener.models import ShortenedUrl
from app.pkg.shortener.services import ShortedUrlService


class ShortenerTestCase(APITestCase):
    create_shortener_url = reverse('shortener-list')
    urls_count_url = reverse('shortener-urls-count')
    most_popular_urls = reverse('most-popular-list')

    url = 'https://www.google.com.ua/'
    url2 = 'https://www.amazon.com/'
    url3 =  'https://www.google.com.ua/test/'
    big_url = 'https://www.google.com/search?q=django&oq=django&aqs=chrome..69i57j69i59l2j69i60j69i61j69i60j' \
    '69i65j69i60.1317j0j7&sourceid=chrome&ie=UTF-8'

    def test_create_shortener_url_201(self):
        response = self.client.post(self.create_shortener_url, data={'url': self.url})
        self.assertTrue(len(response.data['shortened_url']) > 0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_create_from_big_url_201(self):
        response = self.client.post(self.create_shortener_url, data={'url': self.big_url})
        self.assertTrue(len(response.data['shortened_url']) > 0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_follow_url(self):
        ShortedUrlService.create_shorted_url(self.big_url)
        url = ShortenedUrl.objects.get(url=self.big_url).shortened_url
        r = self.client.get(url)
        self.assertEqual(r.headers['LOCATION'], self.big_url)
        self.assertEqual(r.status_code, status.HTTP_302_FOUND)

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
        self.assertEqual(len(response.data['results']), 2)
