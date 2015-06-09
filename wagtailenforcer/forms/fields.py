from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailimages import fields

from django_antivirus_field.utils import is_infected


class WagtailImageField(fields.WagtailImageField):

    def check_if_infected(self, f):
        has_virus, name = is_infected(f.file.read())

        if has_virus:
            raise ValidationError(_('Virus "{}" was detected').format(name))

    def to_python(self, data):
        f = super(WagtailImageField, self).to_python(data)

        if f is not None:
            self.check_if_infected(f)

        return f
