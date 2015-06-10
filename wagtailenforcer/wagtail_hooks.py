from django.core.urlresolvers import reverse

from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.menu import MenuItem


@hooks.register('register_admin_menu_item')
def register_frank_menu_item():
    return MenuItem('Blocked users', reverse('wagtailenforcer_blocked_users'), classnames='icon icon-locked', order=10000)
