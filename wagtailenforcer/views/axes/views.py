
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from django.utils.translation import ugettext as _

from axes.models import AccessAttempt
from axes import utils

from wagtailenforcer.forms.wagtailadmin import SearchForm


@permission_required('wagtailadmin.access_admin')
def list(request):
    """
    View to list all/filtered blocked login attempts
    """
    search_form = SearchForm(request.GET)
    is_searching = False

    # fetch blocked attempts, checking if overridden the failure limit
    FAILURE_LIMIT = getattr(settings, 'AXES_LOGIN_FAILURE_LIMIT', 3)
    attempts = AccessAttempt.objects.filter(failures_since_start__gte=FAILURE_LIMIT)

    if request.GET.get('search_field') and search_form.is_valid():
        search_text = search_form.cleaned_data.get('search_field')
        if search_text:
            attempts = attempts.filter(
                Q(username__icontains=search_text) |
                Q(user_agent__icontains=search_text)
            )
            is_searching = True

    attempts = attempts.order_by('-username')

    if attempts:
        p = request.GET.get('p', 1)
        paginator = Paginator(attempts, 20)

        try:
            attempts = paginator.page(p)
        except PageNotAnInteger:
            attempts = paginator.page(1)
        except EmptyPage:
            attempts = paginator.page(paginator.num_pages)

    return render(request, 'wagtailenforcer/attempts.html', {
        'attempts': attempts,
        'search_form': search_form,
        'is_searching': is_searching
    })


@permission_required('wagtailadmin.access_admin')
def reset(request, id):
    """
    View to reset axes AccessAttempt with given id
    """
    attempt = get_object_or_404(AccessAttempt, id=id)
    success = utils.reset(attempt.ip_address, attempt.username)

    user = attempt.username or attempt.ip_address

    if success > 0:
        messages.success(request, _("User '{0}' unblocked.").format(user))
    else:
        messages.error(request, _("User '{0}' was not blocked.").format(user))

    return HttpResponseRedirect(reverse('wagtailenforcer_blocked_users'))
