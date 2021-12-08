from django.urls import reverse_lazy

from wagtail.admin.views import account as account_views


def password_reset(request, **kwargs):
    from wagtailenforcer.forms.wagtailusers import PasswordResetForm
    kwargs.update({
        'template_name': 'wagtailadmin/account/password_reset/form.html',
        'email_template_name': 'wagtailadmin/account/password_reset/email.txt',
        'subject_template_name': 'wagtailadmin/account/password_reset/email_subject.txt',
        'form_class': PasswordResetForm,
        'success_url': reverse_lazy('wagtailadmin_password_reset_done'),
    })
    return account_views.PasswordResetView.as_view(**kwargs)(request)


def password_reset_done(request, **kwargs):
    kwargs.update({
        'template_name': 'wagtailadmin/account/password_reset/done.html'
    })
    return account_views.PasswordResetDoneView.as_view(**kwargs)(request)


def password_reset_confirm(request, **kwargs):
    from wagtailenforcer.forms.wagtailusers import PasswordForm

    # URL params are part of kwargs, which shouldn't go to the as_view() call
    request_kwargs = {}
    if 'uidb64' in kwargs:
        request_kwargs['uidb64'] = kwargs['uidb64']
        del kwargs['uidb64']

    if 'token' in kwargs:
        request_kwargs['token'] = kwargs['token']
        del kwargs['token']

    kwargs.update({
        'template_name': 'wagtailadmin/account/password_reset/enforce_confirm.html',
        'success_url': reverse_lazy('wagtailadmin_password_reset_complete'),
        'form_class': PasswordForm,
    })
    return account_views.PasswordResetConfirmView.as_view(**kwargs)(request, **request_kwargs)


def password_reset_complete(request, **kwargs):
    kwargs.update({
        'template_name': 'wagtailadmin/account/password_reset/complete.html'
    })
    return account_views.PasswordResetCompleteView.as_view(**kwargs)(request)
