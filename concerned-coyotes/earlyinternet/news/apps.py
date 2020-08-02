import threading

from django.apps import AppConfig
from django.core import management


class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        """ Run thread repeating the news query task """
        background = threading.Thread(
            target=management.call_command, args=['process_tasks'],
            daemon=True
        )
        background.start()
