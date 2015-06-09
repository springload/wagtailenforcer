from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse, NoReverseMatch
from django.contrib import messages

from wagtail.wagtailsearch.backends import get_search_backends

from wagtail.wagtailimages.models import get_image_model
from wagtail.wagtailimages.fields import MAX_UPLOAD_SIZE

from wagtailenforcer.forms.wagtailimages import get_image_form


def edit(request, image_id):
    Image = get_image_model()
    ImageForm = get_image_form()

    image = get_object_or_404(Image, id=image_id)

    if not image.is_editable_by_user(request.user):
        raise PermissionDenied

    if request.POST:
        original_file = image.file
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            if 'file' in form.changed_data:
                # if providing a new image file, delete the old one and all renditions.
                # NB Doing this via original_file.delete() clears the file field,
                # which definitely isn't what we want...
                original_file.storage.delete(original_file.name)
                image.renditions.all().delete()
            form.save()

            # Reindex the image to make sure all tags are indexed
            for backend in get_search_backends():
                backend.add(image)

            messages.success(request, _("Image '{0}' updated.").format(image.title))
            return redirect('wagtailimages_index')
        else:
            messages.error(request, _("The image could not be saved due to errors."))
    else:
        form = ImageForm(instance=image)

    # Check if we should enable the frontend url generator
    try:
        reverse('wagtailimages_serve', args=('foo', '1', 'bar'))
        url_generator_enabled = True
    except NoReverseMatch:
        url_generator_enabled = False

    return render(request, "wagtailimages/images/edit.html", {
        'image': image,
        'form': form,
        'url_generator_enabled': url_generator_enabled,
    })


@permission_required('wagtailimages.add_image')
def add(request):
    ImageForm = get_image_form()
    ImageModel = get_image_model()

    if request.POST:
        image = ImageModel(uploaded_by_user=request.user)
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()

            # Reindex the image to make sure all tags are indexed
            for backend in get_search_backends():
                backend.add(image)

            messages.success(request, _("Image '{0}' added.").format(image.title))
            return redirect('wagtailimages_index')
        else:
            messages.error(request, _("The image could not be created due to errors."))
    else:
        form = ImageForm()

    return render(request, "wagtailimages/images/add.html", {
        'form': form,
        'max_filesize': MAX_UPLOAD_SIZE,
    })
