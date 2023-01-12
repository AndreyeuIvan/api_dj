from django.test import TestCase
from news_api_scrap.models import News


class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.create(title="MyNews", author="Mark Twen")
        News.objects.create(title="BestNews_today", author="Mark Christianson")
