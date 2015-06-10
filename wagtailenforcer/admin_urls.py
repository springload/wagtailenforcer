from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'wagtailenforcer.views.axes.views.list', name='wagtailenforcer_blocked_users'),
    url(r'^/reset/(\d+)/$', 'wagtailenforcer.views.axes.views.reset', name='wagtailenforcer_unblock_user'),
)
