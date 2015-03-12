from django import forms
from django.contrib.auth.models import User
from communityfund.widgets import BSTextInput, BSEmailInput, BSPasswordInput, glyphicon


class SignupForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username, email,
    password, first name and last name.
    """
    error_messages = {
        'duplicate': "A user with that username or email already exists.",
        'password_mismatch': "The two password fields didn't match.",
    }

    first_name = forms.CharField(
        widget=BSTextInput("First Name", hide_label=True), max_length=30, help_text="Required. 30 characters or fewer.")

    last_name = forms.CharField(
        widget=BSTextInput("Last Name", hide_label=True), max_length=30, help_text="Required. 30 characters or fewer.")

    email = forms.EmailField(
        widget=BSEmailInput("Email", hide_label=True, prepended='@'))

    username = forms.RegexField(
        widget=BSTextInput("Username", hide_label=True, prepended=glyphicon('user')), max_length=30,
        regex=r'^[\w.@+-]+$', help_text="Required. 30 characters or fewer. Letters, digits and @.+-_ only.",
        error_messages={'invalid': "This value may contain only letters, numbers and @.+-_ characters."})

    password1 = forms.CharField(
        widget=BSPasswordInput("Password", hide_label=True, prepended=glyphicon('lock')), min_length=8, max_length=128,
        help_text="Required. 8-128 characters.")

    password2 = forms.CharField(
        widget=BSPasswordInput("Confirm Password", hide_label=True, prepended=glyphicon('repeat')), min_length=8,
        max_length=128, help_text="Enter the same password as above, for verification.")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True, login=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user