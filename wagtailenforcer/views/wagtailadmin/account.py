from __future__ import absolute_import, unicode_literals

from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth import update_session_auth_hash
from django.http import Http404
from django.shortcuts import redirect, render

from wagtailenforcer.forms import wagtailadmin

from password_policies.conf import settings
from password_policies.forms import PasswordPoliciesChangeForm


# Helper functions to check password management settings to enable/disable views as appropriate.
# These are functions rather than class-level constants so that they can be overridden in tests
# by override_settings


def password_management_enabled():
    return getattr(settings, "WAGTAIL_PASSWORD_MANAGEMENT_ENABLED", True)


def change_password(request):
    if not password_management_enabled():
        raise Http404

    can_change_password = request.user.has_usable_password()

    if can_change_password:
        if request.method == 'POST':
            form = PasswordPoliciesChangeForm(request.user, request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)

                messages.success(request, _("Your password has been changed successfully!"))
                return redirect('wagtailadmin_account')
        else:
            form = PasswordPoliciesChangeForm(request.user)
    else:
        form = None

    return render(request, 'wagtailadmin/account/change_password.html', {
        'form': form,
        'can_change_password': can_change_password,
    })
