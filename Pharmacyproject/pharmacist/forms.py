from django import forms
from .models import Pharamcist
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class PharmacistLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class PharmacistRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        validators=[validate_password]
    )
    cpassword = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )
    class Meta:
        model = Pharamcist
        fields = ["username", "password", "cpassword", "email", "pharmacy_name", "address","phone_no","license_number","company_pic"]
    
    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")
        return uname
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        cpassword = cleaned_data.get("cpassword")

        if password and cpassword and password != cpassword:
            self.add_error('cpassword', "Passwords And Confirm Password do not match.")

        return cleaned_data
     
