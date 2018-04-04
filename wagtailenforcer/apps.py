from django.apps import AppConfig


class WagtailEnforcerAppConfig(AppConfig):
    name = 'wagtailenforcer'

    def ready(self):
        from wagtailenforcer import signals  # NOQA
