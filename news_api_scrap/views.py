from django.shortcuts import render


def main(request):
    return render(request, 'news_api_scrap/main.html')
