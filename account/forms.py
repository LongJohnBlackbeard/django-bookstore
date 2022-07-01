from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django_countries.widgets import CountrySelectWidget

from .models import UserBase


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Username", "id": "login-username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password", "id": "login-pwd"})
    )


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label="Enter Username", min_length=5, max_length=50, help_text="Required")
    email = forms.EmailField(
        max_length=100, help_text="Required", error_messages={"required": "Sorry, you will need an email."}
    )
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = (
            "user_name",
            "email",
        )

    def clean_usernames(self):
        user_name = self.cleaned_data["user_name"].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return cd["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered with an account.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Username"})
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "E-mail", "name": "email", "id": "id_email"}
        )
        self.fields["password"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Repeat Password"})


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label="Account email (can not be changed)",
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "email", "id": "form-email", "readonly": "readonly"}
        ),
    )

    user_name = forms.CharField(
        label="Username",
        min_length=5,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Username",
                "id": "form-firstname",
                "readonly": "readonly",
            }
        ),
    )

    first_name = forms.CharField(
        label="First Name",
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "First Name", "id": "form-lastname"}
        ),
    )

    # country =  CountryField().formfield(
    #     widget=CountrySelectWidget(
    #         attrs={'class': 'form-control mb-3', 'placeholder': 'Country', 'id': 'form-country'}))

    phone_number = forms.CharField(
        label="Phone Number",
        min_length=10,
        max_length=31,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Phone Number", "id": "form-phone_number"}
        ),
    )

    postcode = forms.CharField(
        label="Postal Code",
        min_length=5,
        max_length=12,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Postal Code", "id": "form-postcode"}
        ),
    )

    address_line_1 = forms.CharField(
        label="Address Line 1",
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Adress Line 1", "id": "form-address_line_1"}
        ),
    )

    address_line_2 = forms.CharField(
        label="Address Line 2",
        required=False,
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Address Line 2", "id": "form-address_line_2"}
        ),
    )

    town_city = forms.CharField(
        label="Town/City",
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Town/City", "id": "form-town_city"}
        ),
    )

    class Meta:
        model = UserBase
        fields = {
            "email",
            "user_name",
            "first_name",
            "country",
            "phone_number",
            "postcode",
            "address_line_1",
            "address_line_2",
            "town_city",
            "town_city",
        }
        widgets = {
            "country": CountrySelectWidget(
                layout='{widget}<img class="country-select-flag" id="{flag_id}" style="margin: 6px 4px 0" src="{country.flag}"><br/>',
                attrs={"class": "form-control"},
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].required = True
        self.fields["email"].required = True
        self.fields["address_line_2"].required = False


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Email", "id": "form-email"}),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationError("Unfortunatley we can not find that email address")
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "New Password", "id": "form-new-pass"}
        ),
    )
    new_password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "New Password", "id": "form-new-pass2"}
        ),
    )
