from django.conf.urls import patterns, url


# Here we put all the new Wagtail admin urls

urlpatterns = patterns(
    '',
    url(r'^$', 'wagtailenforcer.views.axes.views.list', name='wagtailenforcer_blocked_users'),
    url(r'^/reset/(\d+)/$', 'wagtailenforcer.views.axes.views.reset', name='wagtailenforcer_unblock_user'),
)
