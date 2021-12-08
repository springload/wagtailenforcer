from django.apps import AppConfig


class WagtailEnforcerAppConfig(AppConfig):
    name = 'wagtailenforcer'

    def ready(self):
        from django.utils.decorators import method_decorator

        from wagtail.admin.views.account import LoginView as WagtailLoginView
        from wagtailenforcer import signals  # NOQA

        from axes import signals    # NOQA
        from axes.decorators import axes_dispatch
        from axes.decorators import axes_form_invalid

        # replacement for watch_login: https://github.com/jazzband/django-axes/compare/3.0.1...3.0.2
        WagtailLoginView.dispatch = method_decorator(axes_dispatch)(WagtailLoginView.dispatch)
        WagtailLoginView.form_invalid = method_decorator(axes_form_invalid)(WagtailLoginView.form_invalid)
