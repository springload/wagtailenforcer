from django.conf.urls import url
from django.contrib.auth import views as django_auth_views

from wagtail.wagtailadmin.views import account

from axes.decorators import watch_login

from wagtailenforcer.forms import PasswordForm, PasswordResetForm
from wagtailenforcer.views.wagtailusers import users
from wagtailenforcer.views.wagtaildocs import documents, chooser


urlpatterns = [
    # Password reset
    url(
        r'^password_reset/$', 'django.contrib.auth.views.password_reset', {
            'template_name': 'wagtailadmin/account/password_reset/form.html',
            'email_template_name': 'wagtailadmin/account/password_reset/email.txt',
            'subject_template_name': 'wagtailadmin/account/password_reset/email_subject.txt',
            'password_reset_form': PasswordResetForm,
        }, name='password_reset'
    ),
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

    url(r'^users/([^\/]+)/$', users.edit, name='wagtailusers_users_edit'),

    url(r'^documents/add/$', documents.add, name='wagtaildocs_add_document'),
    url(r'^documents/edit/(\d+)/$', documents.edit, name='wagtaildocs_edit_document'),
    url(r'^documents/chooser/$', chooser.chooser, name='wagtaildocs_chooser'),
    url(r'^documents/chooser/upload/$', chooser.chooser_upload, name='wagtaildocs_chooser_upload'),

]
