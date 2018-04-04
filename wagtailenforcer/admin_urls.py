from django.conf.urls import url

from wagtailenforcer.views.axes import views as axes_views

# Here we put all the new Wagtail admin urls

urlpatterns = [
    url(r'^$', axes_views.list, name='wagtailenforcer_blocked_users'),
    url(r'^reset/(\d+)/$', axes_views.reset, name='wagtailenforcer_unblock_user'),
]
