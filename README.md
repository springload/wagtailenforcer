# wagtailenforcer [![PyPI](https://img.shields.io/pypi/v/wagtailenforcer.svg)](https://pypi.python.org/pypi/wagtailenforcer)

> WagtailEnforcer, the strong arm of the law.

If you need to enforce security protocols on your Wagtail site you've come to the right place.

Wagtailenforcer makes use of the following packages to ensure strict password policies and other security protocols are implemented.

* [Password policies](https://github.com/iplweb/django-password-policies-iplweb)
* [Axes](https://github.com/springload/django-axes)

<img src="./cobra.jpg" width="200">

> -  Lt. Marion "Cobra" Cobretti

*Check out [Awesome Wagtail](https://github.com/springload/awesome-wagtail) for more awesome packages and resources from the Wagtail community.*

## Quickstart

```sh
pip install wagtailenforcer
```

Time to edit the **settings.py** file. ```INSTALLED_APPS``` should have:

```python
...
    'axes',
    'password_policies',
    'wagtailenforcer',
...
```

.. and ```MIDDLEWARE_CLASSES```:

```python
    'wagtailenforcer.middleware.WagtailenforcerMiddleware'
```

Some extra settings:

```python
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

In **urls.py**:

```python
from wagtailenforcer import urls as wagtailenforcer_urls

wagtailadmin_urls.urlpatterns = wagtailenforcer_urls + wagtailadmin_urls.urlpatterns
```

Check the docs of the apps if you need to do changes to the predefined settings.

## Development

### Releases

- Make a new branch for the release of the new version.
- Update the [CHANGELOG](https://github.com/springload/wagtailenforcer/CHANGELOG.md).
- Update the version number in `setup.py`, following semver.
- Make a PR and squash merge it.
- Back on master with the PR merged, use `make publish` (confirm, and enter your password).
- Finally, go to GitHub and create a release and a tag for the new version.
- Done!
