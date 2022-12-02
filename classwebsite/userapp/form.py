from django import forms
from django.contrib.auth.models import User
from classwebsite.adminapp.models import Profile


class Customer_form(forms.ModelForm):
    profile_passport = forms.ImageField(required=False, label='Profile_passport')
    particulars = forms.FileField(required=False, label='particulars')
    class Meta:
        model = Profile
        fields = [
            'address',
            'phone_number',
            'nationality',
            'state',
            'particulars',
            'profile_passport',
        ]