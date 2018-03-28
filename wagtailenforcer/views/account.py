from wagtail.wagtailadmin.views import account as account_views


def password_reset(request, **kwargs):
    from wagtailenforcer.forms.wagtailusers import PasswordResetForm
    kwargs.update({
        'template_name': 'wagtailadmin/account/password_reset/form.html',
        'email_template_name': 'wagtailadmin/account/password_reset/email.txt',
        'subject_template_name': 'wagtailadmin/account/password_reset/email_subject.txt',
        'password_reset_form': PasswordResetForm,
        'post_reset_redirect': 'wagtailadmin_password_reset_done',
    })
    return account_views.password_reset(request, **kwargs)


def password_reset_done(request, **kwargs):
    kwargs.update({
        'template_name': 'wagtailadmin/account/password_reset/done.html'
    })
    return account_views.password_reset_done(request, **kwargs)


def password_reset_confirm(request, **kwargs):
    from wagtailenforcer.forms.wagtailusers import PasswordForm
    kwargs.update({
        'template_name': 'wagtailadmin/account/password_reset/enforce_confirm.html',
        'post_reset_redirect': 'wagtailadmin_password_reset_complete',
        'set_password_form': PasswordForm,
        'extra_context': {'reset_password_url': '/admin/password_reset'},
    })
    return account_views.password_reset_confirm(request, **kwargs)


def password_reset_complete(request, **kwargs):
    kwargs.update({
        'template_name': 'wagtailadmin/account/password_reset/complete.html'
    })
    return account_views.password_reset_complete(request, **kwargs)
