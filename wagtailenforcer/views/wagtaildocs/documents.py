from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied

from wagtail.wagtaildocs.models import Document
from wagtail.wagtailsearch.backends import get_search_backends

from wagtailenforcer.forms import DocumentForm


@permission_required('wagtaildocs.add_document')
def add(request):
    """
    Override of wagtaildocs.views.documents.add to use wagtailenforcer.forms.DocumentForm
    """
    if request.POST:
        doc = Document(uploaded_by_user=request.user)
        form = DocumentForm(request.POST, request.FILES, instance=doc)
        if form.is_valid():
            form.save()

            # Reindex the document to make sure all tags are indexed
            for backend in get_search_backends():
                backend.add(doc)

            messages.success(request, _("Document '{0}' added.").format(doc.title))
            return redirect('wagtaildocs_index')
        else:
            messages.error(request, _("The document could not be saved due to errors."))
    else:
        form = DocumentForm()

    return render(request, "wagtaildocs/documents/add.html", {
        'form': form,
    })


@permission_required('wagtailadmin.access_admin')
def edit(request, document_id):
    """
    Override of wagtaildocs.views.documents.edit to use wagtailenforcer.forms.DocumentForm
    """
    doc = get_object_or_404(Document, id=document_id)

    if not doc.is_editable_by_user(request.user):
        raise PermissionDenied

    if request.POST:
        original_file = doc.file
        form = DocumentForm(request.POST, request.FILES, instance=doc)
        if form.is_valid():
            if 'file' in form.changed_data:
                # if providing a new document file, delete the old one.
                # NB Doing this via original_file.delete() clears the file field,
                # which definitely isn't what we want...
                original_file.storage.delete(original_file.name)
            doc = form.save()

            # Reindex the document to make sure all tags are indexed
            for backend in get_search_backends():
                backend.add(doc)

            messages.success(request, _("Document '{0}' updated").format(doc.title))
            return redirect('wagtaildocs_index')
        else:
            messages.error(request, _("The document could not be saved due to errors."))
    else:
        form = DocumentForm(instance=doc)

    return render(request, "wagtaildocs/documents/edit.html", {
        'document': doc,
        'form': form
    })
