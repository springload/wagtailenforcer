
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from axes.models import AccessAttempt


@permission_required('wagtailadmin.access_admin')
def list(request):
    attempts = AccessAttempt.objects.all()

    p = request.GET.get('p', 1)
    paginator = Paginator(attempts, 20)

    try:
        attempts = paginator.page(p)
    except PageNotAnInteger:
        attempts = paginator.page(1)
    except EmptyPage:
        attempts = paginator.page(paginator.num_pages)

    return render(request, 'wagtailenforcer/attempts.html', {'attempts': attempts, })
