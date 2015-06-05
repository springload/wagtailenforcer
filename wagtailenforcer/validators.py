from django.utils.translation import ungettext

from password_policies.forms.validators import LetterCountValidator


class UpperCaseLetterValidator(LetterCountValidator):
    """
    Upper case validator
    """
    categories = ['Lu']

    def get_error_message(self):
        """
        Returns this validator's error message.
        """
        msg = ungettext("The new password must contain %d or more uppercase letter.",
                        "The new password must contain %d or more uppercase letter.",
                        self.get_min_count()) % self.get_min_count()
        return msg
