from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        from django.conf import settings
        if settings.TESTING:
            return

        from .tasks import get_news
        from background_task.models import Task
        get_news(repeat=Task.DAILY, repeat_until=None)
