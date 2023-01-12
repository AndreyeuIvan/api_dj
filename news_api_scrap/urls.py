from django.urls import path
from news_api_scrap.views import main


urlpatterns = [
    path("main/", main, name='main'),
]
