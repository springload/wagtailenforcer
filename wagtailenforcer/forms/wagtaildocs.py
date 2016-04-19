import os

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from wagtail.wagtaildocs import forms

from django_antivirus_field.utils import is_infected

INVALID_DOCUMENT_ERROR = _(
    "Not a supported document format."
)


class DocumentForm(forms.BaseDocumentForm):
    """
    Override of wagtail.wagtaildocs.forms to ensure uploaded file gets scanned before being properly saved
    """
    def clean(self):
        cleaned_data = super(DocumentForm, self).clean()
        field = self.cleaned_data['file']

        if hasattr(settings, 'ALLOWED_DOCUMENT_EXTENSIONS'):
            extension = os.path.splitext(field.name)[1].lower()[1:]

            if extension not in settings.ALLOWED_DOCUMENT_EXTENSIONS:
                self.add_error('file', ValidationError(INVALID_DOCUMENT_ERROR))

        has_virus, name = is_infected(field.file.read())

        if has_virus:
            self.add_error('file', ValidationError(_('Virus "{}" was detected').format(name)))

        return cleaned_data
