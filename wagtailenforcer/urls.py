from django.conf.urls import url
from django.contrib.auth import views as django_auth_views

from wagtail.wagtailadmin.views import account

from axes.decorators import watch_login

from wagtailenforcer.forms import PasswordForm
from wagtailenforcer.views import edit_user


urlpatterns = [
    url(
        r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        django_auth_views.password_reset_confirm, {
            'template_name': 'wagtailadmin/account/password_reset/confirm.html',
            'post_reset_redirect': '/admin/password_reset/complete',
            'set_password_form': PasswordForm,
            'extra_context': {'reset_password_url': '/admin/password_reset'},
        }, name='wagtailadmin_password_reset_confirm',
    ),
    url(r'^login/$', watch_login(account.login), name='wagtailadmin_login'),
    url(r'^users/([^\/]+)/$', edit_user, name='wagtailusers_users_edit'),
]
