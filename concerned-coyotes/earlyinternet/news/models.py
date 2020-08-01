from typing import Dict, Union

from django.db import models
from django.utils.dateparse import parse_datetime


class ArticleManager(models.Manager):

    def create_article(self, raw_article: Dict[str, Union[str, Dict[str, str]]]):

        # convert timezone aware iso date string to datetime.datetime
        published_at = parse_datetime(raw_article['publishedAt'])

        article = self.create(
            source=raw_article['source']['name'],
            author=raw_article['author'],
            title=raw_article['title'],
            description=raw_article['description'],
            content=raw_article['content'],
            url=raw_article['url'],
            published_at=published_at
        )
        return article


class Article(models.Model):

    objects = ArticleManager()
    # now we can do
    # >>> Article.objects.create_article({...})

    source = models.CharField(max_length=256)
    author = models.CharField(default="unknown", max_length=256)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    content = models.CharField(max_length=200)
    url = models.URLField()
    # in utc
    published_at = models.DateTimeField()
