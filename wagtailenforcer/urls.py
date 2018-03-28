from django.conf.urls import url
from django.contrib.auth import views as django_auth_views

from wagtail.wagtailadmin.views import account as wagtail_account_views

from axes.decorators import watch_login

from wagtailenforcer.views import account as account_views
from wagtailenforcer.views.wagtailusers import users

# Here we put all the overriden Wagtail urls from the different wagtail apps

urlpatterns = [
    url(r'^password_reset/$', account_views.password_reset, name='wagtailadmin_password_reset'),
    url(r'^password_reset/done/$', account_views.password_reset_done, name='wagtailadmin_password_reset_done'),
    url(
        r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account_views.password_reset_confirm,
        name='wagtailadmin_password_reset_confirm',
    ),
    url(r'^password_reset/complete/$', account_views.password_reset_complete, name='wagtailadmin_password_reset_complete'),

    url(r'^login/$', watch_login(wagtail_account_views.login), name='wagtailadmin_login'),

    url(r'^users/(\d+)/$', users.edit, name='wagtailusers_users_edit'),
    url(r'^users/new/$', users.create, name='wagtailusers_users_create'),

]
