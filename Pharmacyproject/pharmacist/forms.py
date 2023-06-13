from django import forms
from .models import Pharamcist
from django.contrib.auth.models import User


class PharmacistLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class PharmacistRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Pharamcist
        fields = ["username", "password", "email", "pharmacy_name", "address","phone_no","license_number","company_pic"]

