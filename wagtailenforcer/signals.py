from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.core.signals import got_request_exception
from django.dispatch import receiver
from wagtail.wagtaildocs.models import Document
from wagtail.wagtailimages.models import Image
from .utilities import check_for_virus


if getattr(settings, 'CLAMAV_ACTIVE') == True:
    @receiver(pre_save, sender=Document)
    def pre_file_save(sender, instance, **kwargs):
        instance = check_for_virus(instance)
        instance.clean()


    @receiver(pre_save, sender=Image)
    def pre_image_save(sender, instance, **kwargs):
        instance = check_for_virus(instance)
        instance.clean()
