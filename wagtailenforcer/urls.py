from django.urls import path, re_path
from django.contrib.auth import views as django_auth_views

from wagtail.admin.views.account import LoginView as WagtailLoginView

from wagtailenforcer.views import account as account_views
from wagtailenforcer.views.wagtailadmin.account import change_password
from wagtailenforcer.views.wagtailusers import users

# Here we put all the overriden Wagtail urls from the different wagtail apps

urlpatterns = [
    path('password_reset/', account_views.password_reset, name='wagtailadmin_password_reset'),
    path('password_reset/done/', account_views.password_reset_done, name='wagtailadmin_password_reset_done'),
    re_path(
        r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account_views.password_reset_confirm,
        name='wagtailadmin_password_reset_confirm',
    ),
    path('password_reset/complete/', account_views.password_reset_complete, name='wagtailadmin_password_reset_complete'),

    path('login/', WagtailLoginView.as_view(), name='wagtailadmin_login'),
    # axes watch_login got replaced, look at in apps.ready()
    path('account/change_password/', change_password, name="password_change"),
    re_path(r'^users/(\d+)/$', users.edit, name='wagtailusers_users_edit'),
    path('users/new/', users.create, name='wagtailusers_users_create'),
]
