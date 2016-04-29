wagtailenforcer
==================

<img src="http://www.joblo.com/images_arrownews/172AITHPodcast1.jpg" width="200">

> WagtailEnforcer, the strong arm of the law.
> -  Lt. Marion "Cobra" Cobretti

If you need to enforce security protocols on your Wagtail site you've come to the right place.

Wagtailenforcer makes use of the following packages to ensure strict password policies and other security protocols are implemented.

* [Password policies](https://github.com/tarak/django-password-policies)
* [Axes](https://github.com/springload/django-axes)
* [Antivirus field](https://github.com/budurli/django-antivirus-field)

# Quickstart

```
$ pip install wagtailenforcer

```
Time to edit the **settings.py** file. ```INSTALLED_APPS``` should have:

```
...
    'axes',
    'password_policies',
    'wagtailenforcer',
...
```

.. and ```MIDDLEWARE_CLASSES```:

```
    'axes.middleware.FailedLoginMiddleware',
    'wagtailenforcer.middleware.WagtailenforcerMiddleware'
```

Some extra settings:

```
# Password policy settings
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
PASSWORD_CHECK_ONLY_AT_LOGIN = True
PASSWORD_MIN_LENGTH = 7
PASSWORD_MAX_LENGTH = 25
PASSWORD_HISTORY_COUNT = 6
PASSWORD_MIN_LETTERS = 1
PASSWORD_MIN_NUMBERS = 1
PASSWORD_MIN_SYMBOLS = 1
PASSWORD_DIFFERENCE_DISTANCE = 3

# Django Axes settings
AXES_LOGIN_FAILURE_LIMIT = 5
AXES_LOCK_OUT_AT_FAILURE = True
AXES_ONLY_USER_FAILURES = True  # Lock out based on username and not IP or UserAgent
AXES_LOCKOUT_TEMPLATE = 'wagtailenforcer/lockout.html'

# Antivirus
CLAMAV_ACTIVE = True

# Allowed document uploads extensions
ALLOWED_DOCUMENT_EXTENSIONS = ['pdf']
```

On top of your app **urls.py** file:

```
wagtailadmin_urls.urlpatterns = wagtailenforcer_urls + wagtailadmin_urls.urlpatterns
```

Check the docs of the apps if you need to do changes to the predefined settings.