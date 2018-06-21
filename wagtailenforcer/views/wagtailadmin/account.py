from __future__ import absolute_import, unicode_literals

from functools import wraps

from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import Http404
from django.shortcuts import redirect, render

from wagtail.utils.compat import user_is_authenticated
from wagtailenforcer.forms import wagtailadmin
from wagtail.wagtailadmin.utils import get_available_admin_languages
from wagtail.wagtailcore.models import UserPagePermissionsProxy

from wagtail.wagtailusers.models import UserProfile

from password_policies.conf import settings
from password_policies.forms import PasswordPoliciesChangeForm
from password_policies.forms.fields import PasswordPoliciesField


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
