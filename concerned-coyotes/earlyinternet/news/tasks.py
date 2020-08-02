from background_task import background
from newsapi import NewsApiClient

from .models import Article


API_KEY = "c8a36b9a701d42ca854f7c31de866ba4"


@background()
def get_news():
    """ Query and save top headlines """
    client = NewsApiClient(api_key=API_KEY)
    result = client.get_top_headlines()
    articles = result['articles']
    # save to db
    for article in articles:
        Article.objects.create_article(article)

    return articles
