from django import forms
from django.forms.models import modelform_factory

from wagtail.wagtailimages.models import get_image_model

from wagtailenforcer.forms.fields import WagtailImageField


# Callback to allow us to override the default form field for the image file field
def formfield_for_dbfield(db_field, **kwargs):
    # Check if this is the file field
    if db_field.name == 'file':
        return WagtailImageField(**kwargs)

    # For all other fields, just call its formfield() method.
    return db_field.formfield(**kwargs)


def get_image_form():
    return modelform_factory(
        get_image_model(),
        formfield_callback=formfield_for_dbfield,
        # set the 'file' widget to a FileInput rather than the default ClearableFileInput
        # so that when editing, we don't get the 'currently: ...' banner which is
        # a bit pointless here
        widgets={
            'file': forms.FileInput(),
            'focal_point_x': forms.HiddenInput(attrs={'class': 'focal_point_x'}),
            'focal_point_y': forms.HiddenInput(attrs={'class': 'focal_point_y'}),
            'focal_point_width': forms.HiddenInput(attrs={'class': 'focal_point_width'}),
            'focal_point_height': forms.HiddenInput(attrs={'class': 'focal_point_height'}),
        })
