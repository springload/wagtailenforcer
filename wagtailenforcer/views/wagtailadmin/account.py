import django
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import logout as auth_logout, login as auth_login
from django.utils.translation import ugettext as _ 
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache

from wagtail.wagtailadmin import forms
from wagtail.wagtailusers.forms import NotificationPreferencesForm
from wagtail.wagtailusers.models import UserProfile
from wagtail.wagtailcore.models import UserPagePermissionsProxy


@permission_required('wagtailadmin.access_admin')
def change_password(request):

    if request.POST:
        form = SetPasswordForm(request.user, request.POST)

        if form.is_valid():
            form.save()

            if django.VERSION >= (1, 7):
                from django.contrib.auth import update_session_auth_hash
                update_session_auth_hash(request, form.user)

            messages.success(request, _("Your password has been changed successfully!"))
            return redirect('wagtailadmin_account')
    else:
        form = SetPasswordForm(request.user)

    return render(request, 'wagtailadmin/account/change_password.html', {
        'form': form,
        'can_change_password': can_change_password,
    })
