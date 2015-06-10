from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'wagtailenforcer.views.axes.views.list', name='wagtailenforcer_blocked_users'),
    # url(r'^(\d+)/$', 'lookingforwork.views.axes.attempts', name='submission_view'),
)
