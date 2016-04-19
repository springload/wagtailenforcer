from django.conf.urls import url
from django.contrib.auth import views as django_auth_views

from wagtail.wagtailadmin.views import account

from axes.decorators import watch_login

from wagtailenforcer.forms.wagtailusers import PasswordForm, PasswordResetForm
from wagtailenforcer.views.wagtailusers import users

# Here we put all the overriden Wagtail urls from the different wagtail apps

urlpatterns = [
    url(
        r'^password_reset/$', account.password_reset, {
            'template_name': 'wagtailadmin/account/password_reset/form.html',
            'email_template_name': 'wagtailadmin/account/password_reset/email.txt',
            'subject_template_name': 'wagtailadmin/account/password_reset/email_subject.txt',
            'password_reset_form': PasswordResetForm,
            'post_reset_redirect': 'wagtailadmin_password_reset_done',
        }, name='wagtailadmin_password_reset'
    ),
    url(
        r'^password_reset/done/$', account.password_reset_done, {
            'template_name': 'wagtailadmin/account/password_reset/done.html'
        }, name='wagtailadmin_password_reset_done'
    ),
    url(
        r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account.password_reset_confirm, {
            'template_name': 'wagtailadmin/account/password_reset/enforce_confirm.html',
            'post_reset_redirect': 'wagtailadmin_password_reset_complete',
            'set_password_form': PasswordForm,
            'extra_context': {'reset_password_url': '/admin/password_reset'},
        }, name='wagtailadmin_password_reset_confirm',
    ),
    url(
        r'^password_reset/complete/$', account.password_reset_complete, {
            'template_name': 'wagtailadmin/account/password_reset/complete.html'
        }, name='wagtailadmin_password_reset_complete'
    ),

    url(r'^login/$', watch_login(account.login), name='wagtailadmin_login'),

    url(r'^users/(\d+)/$', users.edit, name='wagtailusers_users_edit'),
    url(r'^users/new/$', users.create, name='wagtailusers_users_create'),

]


# urlpatterns = [
#     url(
#         r'^$', account.password_reset, {
#             'template_name': 'wagtailadmin/account/password_reset/form.html',
#             'email_template_name': 'wagtailadmin/account/password_reset/email.txt',
#             'subject_template_name': 'wagtailadmin/account/password_reset/email_subject.txt',
#             'password_reset_form': PasswordResetForm,
#             'post_reset_redirect': 'wagtailadmin_password_reset_done',
#         }, name='wagtailadmin_password_reset'
#     ),
#     url(
#         r'^done/$', account.password_reset_done, {
#             'template_name': 'wagtailadmin/account/password_reset/done.html'
#         }, name='wagtailadmin_password_reset_done'
#     ),
#     url(
#         r'^confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         account.password_reset_confirm, {
#             'template_name': 'wagtailadmin/account/password_reset/confirm.html',
#             'post_reset_redirect': 'wagtailadmin_password_reset_complete',
#         }, name='wagtailadmin_password_reset_confirm',
#     ),
#     url(
#         r'^complete/$', account.password_reset_complete, {
#             'template_name': 'wagtailadmin/account/password_reset/complete.html'
#         }, name='wagtailadmin_password_reset_complete'
#     ),
# ]
