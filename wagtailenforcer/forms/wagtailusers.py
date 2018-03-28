from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm
from django.utils.translation import ugettext_lazy

from password_policies.conf import settings
from password_policies.forms import PasswordPoliciesForm
from password_policies.forms.fields import PasswordPoliciesField

from wagtail.wagtailusers.forms import UserCreationForm as BaseUserCreationForm

from wagtailenforcer.validators import UpperCaseLetterValidator

User = get_user_model()

standard_fields = set(['email', 'first_name', 'last_name', 'is_superuser', 'groups'])


class PasswordResetForm(BasePasswordResetForm):
    email = forms.EmailField(label=ugettext_lazy("Enter your email address to reset your password"), max_length=254)

    def clean(self):
        cleaned_data = super(PasswordResetForm, self).clean()

        # Find users of this email address
        UserModel = get_user_model()
        email = cleaned_data.get('email')
        if not email:
            raise forms.ValidationError(_("Please fill your email address."))
        active_users = UserModel._default_manager.filter(email__iexact=email, is_active=True)

        if active_users.exists():
            # Check if all users of the email address are LDAP users (and give an error if they are)
            found_non_ldap_user = False
            for user in active_users:
                if user.has_usable_password():
                    found_non_ldap_user = True
                    break

            if not found_non_ldap_user:
                # All found users are LDAP users, give error message
                raise forms.ValidationError(_("Sorry, you cannot reset your password here as your user account is managed by another server."))
        # else:
        #     # No user accounts exist
        #     raise forms.ValidationError(_("This email address is not recognised."))

        return cleaned_data


class PasswordForm(PasswordPoliciesForm):
    """
    Password form enforcing DEA password policy https://www.ict.govt.nz/guidance-and-resources/standards-compliance/authentication-standards/password-standard/6-password-minimum-requirements/
    """
    new_password1 = PasswordPoliciesField(
        label=_("New password"),
        max_length=settings.PASSWORD_MAX_LENGTH,
        min_length=settings.PASSWORD_MIN_LENGTH,
        validators=[UpperCaseLetterValidator()]
    )


class UserCreationForm(BaseUserCreationForm):

    password1 = PasswordPoliciesField(
        label=_("New password"),
        max_length=settings.PASSWORD_MAX_LENGTH,
        min_length=settings.PASSWORD_MIN_LENGTH,
        help_text=_("Leave blank if not changing."),
        validators=[UpperCaseLetterValidator()],
        required=False,
    )


class UserEditForm(forms.ModelForm):

    """
    Intelligently sets up the username field if it is infact a username. If the
    User model has been swapped out, and the username field is an email or
    something else, dont touch it.
    """
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        if User.USERNAME_FIELD == 'username':
            field = self.fields['username']
            field.regex = r"^[\w.@+-]+$"
            field.help_text = _("Required. 30 characters or fewer. Letters, "
                                "digits and @/./+/-/_ only.")
            field.error_messages = field.error_messages.copy()
            field.error_messages.update({
                'invalid': _("This value may contain only letters, numbers "
                             "and @/./+/-/_ characters.")})

    @property
    def username_field(self):
        return self[User.USERNAME_FIELD]

    def separate_username_field(self):
        return User.USERNAME_FIELD not in standard_fields

    required_css_class = "required"

    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

    email = forms.EmailField(required=True, label=_("Email"))
    first_name = forms.CharField(required=True, label=_("First Name"))
    last_name = forms.CharField(required=True, label=_("Last Name"))

    password1 = PasswordPoliciesField(
        label=_("New password"),
        max_length=settings.PASSWORD_MAX_LENGTH,
        min_length=settings.PASSWORD_MIN_LENGTH,
        help_text=_("Leave blank if not changing."),
        validators=[UpperCaseLetterValidator()],
        required=False,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"), required=False,
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    is_superuser = forms.BooleanField(
        label=_("Administrator"),
        required=False,
        help_text=_("Administrators have the ability to manage user accounts.")
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "is_active", "is_superuser", "groups")
        widgets = {
            'groups': forms.CheckboxSelectMultiple
        }

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.exclude(id=self.instance.id).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)

        # users can access django-admin if they are a superuser
        user.is_staff = user.is_superuser

        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            self.save_m2m()
        return user
