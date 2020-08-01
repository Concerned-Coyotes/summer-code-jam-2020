from django.db import models


class Article(models.Model):

    source = models.CharField()
    author = models.CharField()
    title = models.CharField()
    description = models.CharField()
    content = models.CharField(max_length=200)
    url = models.URLField()
    # in utc
    published_at = models.DateTimeField()